# mdf-teaching-optimizer

[English README](./README.md)

审计并优化现有 MarkdownFlow 授课提示词，提升内容覆盖一致性、互动有效性与语法稳定性。

## 适用场景

- 对照课程资料检查当前授课提示词是否漏讲、弱讲或偏义。
- 在不重写整章的前提下优化教学逻辑与互动质量。
- 降低变量使用与 MarkdownFlow 语法不稳定带来的运行风险。

## 边界说明

- 本组件用于“已有提示词优化”，不是从零生成全新课程。
- 不替代人工教学判断，尤其是领域化教学策略决策。
- 输出为优化建议与修订后提示词，不是最终发布内容物。

## 3 分钟快速开始

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
mdf-teaching-optimizer --prompt examples/input_prompt.md --source examples/source_material.md --output output/result.json
python -m json.tool output/result.json | head -n 40
```

## 最小可运行示例

输入：
- [`examples/input_prompt.md`](./examples/input_prompt.md)
- [`examples/source_material.md`](./examples/source_material.md)

输出包含：
- `summary`
- `findings`（风险等级、检查项、改动建议）
- `optimized_prompt`

## 架构：Skill Core + Adapters

- Skill Core：[`src/mdf_teaching_optimizer/core.py`](./src/mdf_teaching_optimizer/core.py)
  - 平台无关的审计与优化逻辑。
- CLI Adapter：[`src/mdf_teaching_optimizer/cli.py`](./src/mdf_teaching_optimizer/cli.py)
  - 可在本地与流水线直接运行。
- OpenClaw Adapter：[`adapters/openclaw`](./adapters/openclaw)
- Claude Adapter：[`adapters/claude`](./adapters/claude)
- Codex Adapter：[`adapters/codex`](./adapters/codex)

## 多 Agent 兼容

- OpenClaw 调用示例：[`examples/openclaw_call.md`](./examples/openclaw_call.md)
- Claude 调用示例：[`examples/claude_call.md`](./examples/claude_call.md)
- Codex 调用示例：[`examples/codex_call.md`](./examples/codex_call.md)

## 与 AI-Shifu 的关系

该仓库是 AI-Shifu 课程生产链路中的可复用优化组件之一。

- 官网：https://ai-shifu.com

## 开发

```bash
pip install -e ".[dev]"
ruff check .
pytest -q
```
