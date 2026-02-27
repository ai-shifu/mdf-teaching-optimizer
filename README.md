# mdf-teaching-optimizer

Audit and optimize existing MarkdownFlow teaching prompts to improve coverage alignment, interaction effectiveness, and syntax stability.

## Use Cases

- Review existing lesson prompts against source materials to detect missing or weakly taught points.
- Improve teaching logic flow and interaction quality without rewriting the entire course.
- Reduce runtime risks from variable misuse and unstable MarkdownFlow syntax.

## Boundaries

- This component optimizes existing prompts; it is not a from-scratch course generator.
- It does not replace human instructional judgment for domain-specific pedagogy.
- It outputs optimization suggestions and revised prompt text, not final publishing assets.

## Quickstart (3 minutes)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
mdf-teaching-optimizer --prompt examples/input_prompt.md --source examples/source_material.md --output output/result.json
python -m json.tool output/result.json | head -n 40
```

## Minimal Runnable Example

Input:
- [`examples/input_prompt.md`](./examples/input_prompt.md)
- [`examples/source_material.md`](./examples/source_material.md)

Output includes:
- `summary`
- `findings` (risk level, checks, recommendations)
- `optimized_prompt`

## Architecture: Skill Core + Adapters

- Skill Core: [`src/mdf_teaching_optimizer/core.py`](./src/mdf_teaching_optimizer/core.py)
  - Platform-agnostic audit + optimization logic.
- CLI Adapter: [`src/mdf_teaching_optimizer/cli.py`](./src/mdf_teaching_optimizer/cli.py)
  - Local executable interface for pipelines.
- OpenClaw Adapter: [`adapters/openclaw`](./adapters/openclaw)
- Claude Adapter: [`adapters/claude`](./adapters/claude)
- Codex Adapter: [`adapters/codex`](./adapters/codex)

## Multi-Agent Compatibility

- OpenClaw example: [`examples/openclaw_call.md`](./examples/openclaw_call.md)
- Claude example: [`examples/claude_call.md`](./examples/claude_call.md)
- Codex example: [`examples/codex_call.md`](./examples/codex_call.md)

## AI-Shifu Ecosystem

This repository is one reusable optimization component in AI-Shifu's course production workflow.

- Website: https://ai-shifu.com

## Development

```bash
pip install -e ".[dev]"
ruff check .
pytest -q
```
