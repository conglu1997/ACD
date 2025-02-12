class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"criteria": "Generate a joke that involves a pun about fruits, has a clear setup and punchline, and is suitable for a dinner party."},
            "2": {"joke": "I told my computer I needed a break, and now it won't stop sending me Kit-Kats."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'criteria' in t:
            return f"""Your task is to generate a joke based on the following criteria:
{t['criteria']}

Ensure that your joke is funny, involves a pun about fruits, has a clear setup and punchline, and is suitable for a dinner party. Provide your response in plain text format."""
        else:
            return f"""Your task is to interpret the humor in the following joke:
{t['joke']}

Explain why this joke is funny. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if 'criteria' in t:
            criteria.append("The joke should involve a pun about fruits, have a clear setup and punchline, be funny, and be suitable for a dinner party.")
        else:
            criteria.append("The response should correctly interpret why the joke is funny.")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
