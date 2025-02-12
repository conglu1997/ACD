class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"setup": "Why don't scientists trust atoms?"},
            "2": {"criteria": "Generate a joke involving a play on words about programming, ensuring it is suitable for a workplace environment."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'setup' in t:
            return f"""Your task is to recognize the punchline of the following joke setup and explain why it is funny.

Setup: {t['setup']}

Your response should include:
1. The punchline of the joke.
2. An explanation of why the joke is funny.

Provide your response in plain text format."""
        elif 'criteria' in t:
            return f"""Your task is to generate a joke based on the following criteria:

Criteria: {t['criteria']}

Ensure that your joke adheres to the given criteria and is humorous. Avoid any inappropriate or offensive content.

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'setup' in t:
            criteria = [
                "The response should include the correct punchline.",
                "The explanation should accurately describe why the joke is funny."
            ]
        else:
            criteria = [
                "The response should include a joke that adheres to the given criteria.",
                "The joke should be humorous.",
                "The joke should be appropriate for a workplace environment."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
