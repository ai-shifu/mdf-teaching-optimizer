from mdf_teaching_optimizer.core import audit_and_optimize


def test_optimizer_generates_recommendations_and_output() -> None:
    prompt = """# 示例课节
这是一个没有互动也没有分镜的段落。
"""
    result = audit_and_optimize(prompt)
    assert result["findings"]["risk_level"] in {"medium", "high"}
    assert result["findings"]["interaction_count"] == 0
    assert "?[%{{focus_check}}" in result["optimized_prompt"]
