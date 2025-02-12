class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"analogy": "A caterpillar is to a butterfly as a seed is to a tree.", "task_type": "interpretation"},
            "2": {"criteria": "Generate an analogy to describe the relationship between curiosity and knowledge.", "task_type": "generation"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'interpretation':
            return f"""Interpret the following analogy and explain its meaning:

Analogy: {t['analogy']}

Your explanation should include:
1. A clear interpretation of the relationships in the analogy.
2. An analysis of why this analogy is effective.
3. Examples or scenarios where this analogy might be used.

Submit your response as a plain text string with clearly labeled sections for 'Interpretation', 'Analysis', and 'Examples'."""
        else:
            return f"""Generate an analogy based on the given criteria:

Criteria: {t['criteria']}

Your analogy should:
1. Clearly convey the relationship described in the criteria.
2. Be creative and original.
3. Include a brief explanation of why this analogy is effective.

Submit your response as a plain text string with clearly labeled sections for 'Analogy' and 'Explanation'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'interpretation':
            criteria = [
                "The response should include a clear interpretation of the relationships in the analogy.",
                "The response should include an analysis of why the analogy is effective.",
                "The response should include examples or scenarios where the analogy might be used."
            ]
        else:
            criteria = [
                "The response should clearly convey the relationship described in the criteria.",
                "The response should be creative and original.",
                "The response should include a brief explanation of why the analogy is effective."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
