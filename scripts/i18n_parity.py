"""Compare each locale tree against the default-language tree.

Reports two classes of gap:

1. **Missing files** — a base page with no counterpart in the locale.
2. **Structural drift** — a counterpart exists but its shape differs:
   fewer code blocks, headings, or components than the base page.

Structural drift is the case a plain file-existence check misses. A locale page
can exist, pass a presence check, and still be a stub that dropped every code
example. Prose length is deliberately *not* compared: translations legitimately
differ in length, but a `curl` example does not translate away.

Exit code is 0 unless --strict is passed, matching the informational posture of
the parity workflow (translations lag on purpose).
"""

import argparse
import os
import pathlib
import re
import sys

LOCALES = ("ar", "es", "hi", "zh")

EXEMPT_FILE = ".i18n-exempt"

EXCLUDED_NAMES = {"README.md", "AGENTS.md", "CONTRIBUTING.md"}
EXCLUDED_DIRS = (".github", "node_modules", "snippets", "sdks")

# Components whose absence changes what a reader can actually do, as opposed to
# styling choices a translator may reasonably vary.
COMPONENTS = ("Card", "CardGroup", "Step", "Steps", "CodeGroup", "Accordion", "Tabs")

FENCE_RE = re.compile(r"^[ \t]*```", re.MULTILINE)
HEADING_RE = re.compile(r"^(#{2,4})\s+\S", re.MULTILINE)
FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
SNIPPET_RE = re.compile(r'^import\s+\w+\s+from\s+"/snippets/', re.MULTILINE)


def shape(text: str) -> dict[str, int]:
    """Count structural elements that should survive translation."""
    body = FRONTMATTER_RE.sub("", text)
    counts = {
        # A shared snippet holds real examples, so it counts alongside inline
        # fences. Without this, moving examples into /snippets would blind the
        # check to a locale that dropped one.
        "code blocks": len(FENCE_RE.findall(body)) // 2 + len(SNIPPET_RE.findall(text)),
        "headings": len(HEADING_RE.findall(body)),
    }
    for name in COMPONENTS:
        # Match `<Card ` and `<Card\n` but not `<CardGroup`.
        counts[f"<{name}>"] = len(re.findall(rf"<{name}(?=[\s/>])", body))
    return counts


def base_pages(root: pathlib.Path) -> list[pathlib.Path]:
    """Translatable pages in the default-language tree, as relative paths."""
    out = []
    for path in sorted(root.rglob("*")):
        if path.suffix not in (".md", ".mdx") or not path.is_file():
            continue
        rel = path.relative_to(root)
        if rel.parts[0] in LOCALES or rel.parts[0] in EXCLUDED_DIRS:
            continue
        if any(part.startswith(".") for part in rel.parts):
            continue
        if rel.name in EXCLUDED_NAMES:
            continue
        out.append(rel)
    return out


def compare(root: pathlib.Path, rel: pathlib.Path, locale: str) -> list[str]:
    """Return human-readable deficits for one locale page, or []."""
    target = root / locale / rel
    if not target.is_file():
        return ["missing"]

    base_shape = shape((root / rel).read_text(encoding="utf-8"))
    loc_shape = shape(target.read_text(encoding="utf-8"))

    # Only a *deficit* is a problem. A locale page with extra examples is fine.
    return [
        f"{key} {loc_shape[key]}/{expected}"
        for key, expected in base_shape.items()
        if loc_shape[key] < expected
    ]


def read_exemptions(root: pathlib.Path) -> set[str]:
    """Paths excused from parity, one per line in .i18n-exempt, `#` comments."""
    path = root / EXEMPT_FILE
    if not path.is_file():
        return set()
    out = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        entry = line.split("#", 1)[0].strip()
        if entry:
            out.add(entry)
    return out


def build_report(root: pathlib.Path) -> tuple[str, int]:
    """Render the markdown parity report and count total gaps."""
    exempt = read_exemptions(root)
    all_pages = base_pages(root)
    pages = [p for p in all_pages if str(p) not in exempt]
    skipped = sorted(str(p) for p in all_pages if str(p) in exempt)

    lines = [
        "## i18n parity report",
        "",
        f"Base tree: {len(pages)} translatable page(s)",
    ]
    if skipped:
        lines += [
            "",
            f"Exempt via `{EXEMPT_FILE}`: " + ", ".join(f"`{p}`" for p in skipped),
        ]
    lines.append("")
    total_gaps = 0

    for locale in LOCALES:
        if not (root / locale).is_dir():
            lines.append(f"- `{locale}/` — locale directory missing")
            total_gaps += 1
            continue

        missing: list[pathlib.Path] = []
        drifted: list[tuple[pathlib.Path, list[str]]] = []
        for rel in pages:
            deficits = compare(root, rel, locale)
            if deficits == ["missing"]:
                missing.append(rel)
            elif deficits:
                drifted.append((rel, deficits))

        ok = len(pages) - len(missing) - len(drifted)
        total_gaps += len(missing) + len(drifted)
        lines.append(
            f"- `{locale}/` — {ok}/{len(pages)} at parity "
            f"({len(missing)} missing, {len(drifted)} structurally short)"
        )
        lines += [f"  - missing: `{locale}/{rel}`" for rel in missing]
        lines += [
            f"  - short: `{locale}/{rel}` — {', '.join(deficits)}"
            for rel, deficits in drifted
        ]

    lines += ["", f"**{total_gaps} gap(s) across {len(LOCALES)} locale(s).**"]
    return "\n".join(lines), total_gaps


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", type=pathlib.Path)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="exit non-zero when any locale page is missing or structurally short",
    )
    args = parser.parse_args()

    report, total_gaps = build_report(args.root.resolve())
    print(report)

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as handle:
            handle.write(report + "\n")

    return 1 if (args.strict and total_gaps) else 0


if __name__ == "__main__":
    sys.exit(main())
