class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"pattern": [[1, 0, 1], [0, 1, 0], [1, 0, 1]], "rule": "mirror horizontally"},
            "2": {"pattern": [[1, 1, 0], [0, 1, 1], [1, 0, 0]], "rule": "rotate 90 degrees clockwise"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        pattern = t["pattern"]
        rule = t["rule"]
        pattern_str = '\n'.join([str(row) for row in pattern])
        return f"""Identify or generate the visual pattern based on the following rule: {rule}. The initial pattern is:
{pattern_str}

Rule Definitions:
- "mirror horizontally": Flip the pattern horizontally along the vertical axis. For example, [[1, 0], [0, 1]] becomes [[0, 1], [1, 0]].
- "rotate 90 degrees clockwise": Rotate the pattern 90 degrees in the clockwise direction. For example, [[1, 0], [0, 1]] becomes [[0, 1], [1, 0]].

Submit your response as a list of lists representing the new pattern. For example, if the pattern is mirrored horizontally, submit the new pattern in the format [[1, 0, 1], [0, 1, 0], [1, 0, 1]]."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should correctly apply the given rule to the initial pattern."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
