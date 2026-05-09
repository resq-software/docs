"""Splice each SDK's _pages.json into docs.json's `Generated API Reference`
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


def build_lang_group(language: str, prefix: str, pages_path: pathlib.Path,
                     readme_id: str) -> dict:
    raw = json.loads(pages_path.read_text())
    tree: dict = {}
    for p in raw:
        if p == "README":
            continue
        # p is something like "components/accordion/README" or "Foo/Bar"
        parts = normalize_path(p)
        full_id = f"{prefix}/{p}" if not p.endswith("/README") else f"{prefix}/{p}"
        full_id = f"{prefix}/{p}"
        insert(tree, parts, full_id)
    pages = [readme_id] + to_mintlify(tree, None)
    return {"group": language, "pages": pages}


def main() -> int:
    docs_json_path = pathlib.Path("docs.json")
    docs = json.loads(docs_json_path.read_text())

    lang_specs = [
        ("TypeScript", "typescript", "sdks/typescript/api"),
        (".NET",       "dotnet",     "sdks/dotnet/api"),
        ("Python",     "python",     "sdks/python/api"),
    ]

    new_subgroups = []
    for label, lang, prefix in lang_specs:
        pages_path = pathlib.Path(prefix) / "_pages.json"
        if not pages_path.exists():
            print(f"SKIP {label}: {pages_path} not found", file=sys.stderr)
            continue
        readme_id = f"{prefix}/README"
        new_subgroups.append(build_lang_group(label, prefix, pages_path, readme_id))

    # Find Generated API Reference under en > SDKs > groups
    en = next(l for l in docs["navigation"]["languages"] if l["language"] == "en")
    sdks_tab = next(t for t in en["tabs"] if t["tab"] == "SDKs")
    gen_group = next(
        g for g in sdks_tab["groups"]
        if g["group"] == "Generated API Reference"
    )
    gen_group["pages"] = new_subgroups

    docs_json_path.write_text(json.dumps(docs, indent=2, ensure_ascii=False) + "\n")
    print(f"Updated docs.json with {sum(1 for _ in new_subgroups)} language groups")
    return 0


if __name__ == "__main__":
    sys.exit(main())
