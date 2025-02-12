class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {"scenario": "A bustling city street at night with neon lights and people hurrying by.", "style": "William Shakespeare"},
            "2": {"scenario": "A serene countryside landscape with rolling hills and a small cottage.", "style": "Vincent van Gogh"}
        }
        assert len(tasks) == 2, "There should be exactly two tasks."
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following scenario and rewrite it in the style of {t['style']}:

Scenario: {t['scenario']}

Ensure that your response captures the unique stylistic elements and tone of {t['style']}. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [f"The response should accurately capture the style and tone of {t['style']}."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
