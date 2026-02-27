from __future__ import annotations

import argparse
import json
from pathlib import Path

from .core import audit_and_optimize


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Audit and optimize existing MarkdownFlow teaching prompts for "
            "coverage, interaction quality, and syntax stability."
        )
    )
    parser.add_argument("--prompt", required=True, help="Input teaching prompt markdown path")
    parser.add_argument("--source", default="", help="Optional source material path")
    parser.add_argument("--output", required=True, help="Output JSON path")
    return parser


def main() -> None:
    args = _build_parser().parse_args()
    prompt_text = Path(args.prompt).read_text(encoding="utf-8")
    source_text = ""
    if args.source:
        source_text = Path(args.source).read_text(encoding="utf-8")

    result = audit_and_optimize(prompt_text, source_text)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
