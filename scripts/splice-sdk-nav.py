"""Splice each SDK's _pages.json into docs.json's `Generated Package References`
sub-group for that language.

Builds a hierarchical groups structure from page IDs of the form
`sdks/<lang>/api/<seg>/<seg>/.../<file>`. Each non-leaf directory becomes
a nested group; leaves are page IDs.
"""
import json
import pathlib
import sys


def normalize_path(rel: str) -> list[str]:
    """Drop trailing /README so directory groups don't have a duplicate
    'README' leaf next to the group itself."""
    if rel.endswith("/README"):
        return rel[: -len("/README")].split("/")
    return rel.split("/")


def insert(tree: dict, parts: list[str], full_id: str) -> None:
    if not parts:
        return
    if len(parts) == 1:
        tree.setdefault("_files", []).append((parts[0], full_id))
        return
    head, *rest = parts
    sub = tree.setdefault("_dirs", {}).setdefault(head, {})
    insert(sub, rest, full_id)


def to_mintlify(tree: dict, group_name: str | None) -> dict | list:
    """Convert internal tree to Mintlify groups/pages structure."""
    pages: list = []
    for fname, full_id in sorted(tree.get("_files", [])):
        pages.append(full_id)
    for dname, subtree in sorted(tree.get("_dirs", {}).items()):
        pages.append(to_mintlify(subtree, dname))
    if group_name is None:
        return pages
    return {"group": group_name, "pages": pages}


def group_dotnet_namespace(prefix: str, namespace: str, file_ids: list[str]) -> list:
    """DefaultDocumentation flattens every type, constructor, property, and
    method as a sibling file under the namespace dir, with dotted names
    like `ResQ.Clients.AuthResponse.Token`. Group those by class so the
    sidebar reads `AuthResponse > Token / Type / ctor` rather than 76
    flat siblings. The namespace overview itself (file named exactly
    `<namespace>`) is emitted first as a leaf."""
    members_by_class: dict[str, list[str]] = {}
    namespace_overview: str | None = None

    for full_id in file_ids:
        fname = full_id.split("/")[-1]
        if fname == namespace:
            namespace_overview = full_id
            continue
        if not fname.startswith(namespace + "."):
            members_by_class.setdefault("__misc__", []).append(full_id)
            continue
        rest = fname[len(namespace) + 1:]
        class_name = rest.split(".")[0]
        members_by_class.setdefault(class_name, []).append(full_id)

    pages: list = []
    if namespace_overview:
        pages.append(namespace_overview)

    for class_name in sorted(members_by_class):
        if class_name == "__misc__":
            continue
        members = sorted(members_by_class[class_name])
        class_page_id = f"{prefix}/{namespace}.{class_name}"
        if class_page_id in members:
            ordered = [class_page_id] + [m for m in members if m != class_page_id]
        else:
            ordered = members
        if len(ordered) == 1:
            pages.append(ordered[0])
        else:
            pages.append({"group": class_name, "pages": ordered})

    if "__misc__" in members_by_class:
        pages.extend(sorted(members_by_class["__misc__"]))

    return pages


def is_dotnet_namespace_dir(prefix: str, dirname: str, files: list[str]) -> bool:
    """Heuristic: a .NET namespace dir under sdks/dotnet/api/ has files
    named `<dirname>.<rest>` or exactly `<dirname>`."""
    if "sdks/dotnet/api" not in prefix:
        return False
    return all(
        f.endswith("/" + dirname) or f"/{dirname}." in f
        for f in files
    )


def build_lang_group(language: str, prefix: str, pages_path: pathlib.Path,
                     readme_id: str) -> dict:
    raw = json.loads(pages_path.read_text())
    tree: dict = {}
    for p in raw:
        if p in ("README", "index"):
            continue
        # `<dir>/index.md` is Mintlify's native directory landing page;
        # registering the bare `<dir>` form lets the resolver pick it
        # up natively. `/README` is handled the same way for legacy
        # entries that haven't been renamed yet. Files that don't end
        # in either suffix keep their path verbatim.
        if p.endswith("/index") or p.endswith("/README"):
            bare = p.rsplit("/", 1)[0]
            full_id = f"{prefix}/{bare}"
            parts = bare.split("/")
        else:
            full_id = f"{prefix}/{p}"
            parts = p.split("/")
        insert(tree, parts, full_id)
    pages = [readme_id] + to_mintlify(tree, None)

    # Post-process: collapse .NET namespace dirs into class-grouped form
    if "sdks/dotnet/api" in prefix:
        pages = _collapse_dotnet_classes(pages, prefix)

    return {"group": language, "pages": pages}


def _collapse_dotnet_classes(pages: list, prefix: str) -> list:
    """Walk the rendered pages list. For each top-level group whose
    name matches a .NET namespace pattern (contains `.` and the contained
    file IDs follow the dotted-name convention), replace its pages list
    with the class-grouped form."""
    out: list = []
    for entry in pages:
        if isinstance(entry, dict) and "." in entry.get("group", ""):
            namespace = entry["group"]
            file_ids = [p for p in entry["pages"] if isinstance(p, str)]
            if file_ids and is_dotnet_namespace_dir(prefix, namespace, file_ids):
                regrouped = group_dotnet_namespace(prefix, namespace, file_ids)
                out.append({"group": namespace, "pages": regrouped})
                continue
        out.append(entry)
    return out


def main() -> int:
    docs_json_path = pathlib.Path("docs.json")
    docs = json.loads(docs_json_path.read_text())

    lang_specs = [
        ("TypeScript", "typescript", "sdks/typescript/api"),
        (".NET",       "dotnet",     "sdks/dotnet/api"),
        ("Python",     "python",     "sdks/python/api"),
        ("Rust",       "rust",       "sdks/rust/api"),
        ("C++",        "cpp",        "sdks/cpp/api"),
    ]

    new_subgroups = []
    for label, lang, prefix in lang_specs:
        pages_path = pathlib.Path(prefix) / "_pages.json"
        if not pages_path.exists():
            print(f"SKIP {label}: {pages_path} not found", file=sys.stderr)
            continue
        readme_id = f"{prefix}/README"
        new_subgroups.append(build_lang_group(label, prefix, pages_path, readme_id))

    # Find Generated Package References under en > SDKs > groups
    en = next(l for l in docs["navigation"]["languages"] if l["language"] == "en")
    sdks_tab = next(t for t in en["tabs"] if t["tab"] == "SDKs")
    gen_group = next(
        g for g in sdks_tab["groups"]
        if g["group"] == "Generated Package References"
    )
    gen_group["pages"] = new_subgroups

    docs_json_path.write_text(json.dumps(docs, indent=2, ensure_ascii=False) + "\n")
    print(f"Updated docs.json with {sum(1 for _ in new_subgroups)} language groups")
    return 0


if __name__ == "__main__":
    sys.exit(main())
