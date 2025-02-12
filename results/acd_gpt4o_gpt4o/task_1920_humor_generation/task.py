class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are at a job interview, and the interviewer asks you to tell a joke to lighten the mood. The joke should be professional and suitable for a workplace setting."},
            "2": {"scenario": "You are giving a best man speech at a wedding and want to include a light-hearted joke about the groom. Ensure the joke is respectful and appropriate for all ages."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a humorous response or joke based on the given scenario.

Scenario: {t['scenario']}

Ensure that your joke is contextually appropriate, light-hearted, and likely to amuse the audience in the given scenario. Avoid any offensive or inappropriate content. Provide your response in plain text format as follows:

Joke: [Your joke]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The joke should be contextually appropriate.",
            "The joke should be light-hearted and likely to amuse the audience.",
            "The joke should avoid any offensive or inappropriate content."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
