# Pipeline Schema（统一版）

## 目标
为四个 skills 提供统一可串联的结构化产物，降低调试与组合成本。

## 推荐产物
- `segments.json`
- `lesson_index.json`
- `variables_registry.json`
- `audit_report.json`

## 顶层版本头（每个 JSON 都包含）
- `schema_version`
- `generator_version`
- `source_hash`

## 兼容策略
- Minor 变更：仅追加字段，不改变既有字段语义。
- Major 变更：字段语义变更或删除字段时，提升 `schema_version` 主版本。
- 消费方按 `schema_version` 做向后兼容分支。
