class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"metaphor": "Time is a thief.", "task_type": "interpretation"},
            "2": {"criteria": "Generate a metaphor to describe the feeling of hope.", "task_type": "generation"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'interpretation':
            return f"""Interpret the following metaphor and explain its meaning:

Metaphor: {t['metaphor']}

Your explanation should include:
1. A clear interpretation of the metaphor's meaning.
2. An analysis of why this metaphor is effective.
3. Examples or scenarios where this metaphor might be used.

Submit your response as a plain text string with clearly labeled sections for 'Interpretation', 'Analysis', and 'Examples'."""
        else:
            return f"""Generate a metaphor based on the given criteria:

Criteria: {t['criteria']}

Your metaphor should:
1. Clearly convey the concept described in the criteria.
2. Be creative and original.
3. Include a brief explanation of why this metaphor is effective.

Submit your response as a plain text string with clearly labeled sections for 'Metaphor' and 'Explanation'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'interpretation':
            criteria = [
                "The response should include a clear interpretation of the metaphor's meaning.",
                "The response should include an analysis of why the metaphor is effective.",
                "The response should include examples or scenarios where the metaphor might be used."
            ]
        else:
            criteria = [
                "The response should clearly convey the concept described in the criteria.",
                "The response should be creative and original.",
                "The response should include a brief explanation of why the metaphor is effective."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
