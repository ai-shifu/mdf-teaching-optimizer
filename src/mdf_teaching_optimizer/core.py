from __future__ import annotations

import re
from typing import Any


def _count_interactions(prompt: str) -> int:
    return len(re.findall(r"\?\[%\{\{.*?\}\}", prompt))


def _has_segment_separator(prompt: str) -> bool:
    return "---" in prompt


def _has_deterministic_block(prompt: str) -> bool:
    return "===" in prompt


def _extract_variables(prompt: str) -> list[str]:
    vars_found = re.findall(r"\{\{([a-zA-Z0-9_]+)\}\}", prompt)
    ordered: list[str] = []
    for var in vars_found:
        if var not in ordered:
            ordered.append(var)
    return ordered


def _build_recommendations(prompt: str, interaction_count: int) -> list[str]:
    recs: list[str] = []
    if interaction_count == 0:
        recs.append("至少增加 1 个合法 MDF 互动，且采集后即时反馈并分流。")
    if interaction_count > 5:
        recs.append("单节互动数量超过 5，建议压缩到 3-5 个。")
    if not _has_segment_separator(prompt):
        recs.append("知识段落之间建议增加 `---`，形成讲述节奏。")
    if not _has_deterministic_block(prompt):
        recs.append("建议在目标或总结位置加入 `===固定文本===` 强化确定性输出。")
    if "viewpoint_check" in prompt and "如果你选择" not in prompt:
        recs.append("`viewpoint_check` 需要按选项分叉反馈，避免统一模板。")
    if "SVG" not in prompt and "svg" not in prompt:
        recs.append("核心知识点建议补充 SVG/HTML 可视化任务并紧跟文字讲解图。")
    return recs


def _build_optimized_prompt(prompt: str) -> str:
    optimized = prompt
    if "---" not in optimized:
        optimized = optimized.strip() + "\n\n---\n"
    if "===本节目标" not in optimized:
        optimized = "===本节目标：完成可执行学习闭环===\n\n" + optimized
    if "?[%{{" not in optimized:
        optimized += (
            "\n\n?[%{{focus_check}} 我已理解核心机制 | 我理解部分机制 | 我仍然困惑]"
            "\n你选择的是：{{focus_check}}，我会按你的状态调整讲解深度与下一步任务。\n"
        )
    if "SVG" not in optimized and "svg" not in optimized:
        optimized += (
            "\n!===\n[可视化任务]\n请生成 SVG 结构图，并在图后解释机制成立边界与失效条件。\n!===\n"
        )
    return optimized


def audit_and_optimize(teaching_prompt: str, source_material: str = "") -> dict[str, Any]:
    interaction_count = _count_interactions(teaching_prompt)
    variables = _extract_variables(teaching_prompt)
    recommendations = _build_recommendations(teaching_prompt, interaction_count)
    optimized_prompt = _build_optimized_prompt(teaching_prompt)

    risk_level = "low"
    if interaction_count == 0 or interaction_count > 5:
        risk_level = "high"
    elif recommendations:
        risk_level = "medium"

    findings = {
        "risk_level": risk_level,
        "interaction_count": interaction_count,
        "variables": variables,
        "checks": {
            "has_segment_separator": _has_segment_separator(teaching_prompt),
            "has_deterministic_block": _has_deterministic_block(teaching_prompt),
            "mentions_visualization": ("SVG" in teaching_prompt or "svg" in teaching_prompt),
            "source_material_attached": bool(source_material.strip()),
        },
        "recommendations": recommendations,
    }

    return {
        "summary": "先给结论与风险等级，再给改动点清单。",
        "findings": findings,
        "optimized_prompt": optimized_prompt,
    }
