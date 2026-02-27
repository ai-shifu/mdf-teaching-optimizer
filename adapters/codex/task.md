# Codex Adapter Task

Run in repo root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
mdf-teaching-optimizer --prompt examples/input_prompt.md --source examples/source_material.md --output output/result.json
python -m json.tool output/result.json | head -n 40
```

Codex should use:
- `findings.risk_level`
- `findings.recommendations`
- `optimized_prompt`
