class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"proverb": "A stitch in time saves nine."},
            "2": {"theme": "perseverance"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'proverb' in t:
            return f"""Your task is to interpret the following proverb and explain its meaning and practical application.

Proverb: {t['proverb']}

Your response should include:
1. The meaning of the proverb.
2. An example of a situation where this proverb can be applied.

Provide your response in the following format:
1. Meaning: [your interpretation]
2. Application: [practical example]
Provide your response in plain text format."""
        elif 'theme' in t:
            return f"""Your task is to create a new proverb based on the following theme:

Theme: {t['theme']}

Ensure that your proverb is meaningful, concise, and captures the essence of the given theme. Provide your response in the following format:
Proverb: [your created proverb]
Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'proverb' in t:
            criteria = [
                "The response should include an accurate interpretation of the proverb.",
                "The explanation should provide a practical example of the proverb's application."
            ]
        else:
            criteria = [
                "The response should include a proverb that adheres to the given theme.",
                "The proverb should be meaningful and concise.",
                "The proverb should capture the essence of the theme."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
