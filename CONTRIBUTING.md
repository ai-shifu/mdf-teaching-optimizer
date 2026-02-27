# Contributing

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
ruff check .
pytest -q
```

## Contribution Rules

- Keep behavior aligned with `SKILL.md` and `references/`.
- Preserve optimization boundaries: audit/optimize existing prompts, not full rewrite by default.
- Add tests for any behavior change in checks/recommendations.
- Update docs/examples when interfaces or contracts change.
