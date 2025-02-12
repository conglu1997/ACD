class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"culture": "American", "context": "workplace"},
            "2": {"culture": "British", "context": "pub"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a joke that is culturally relevant to the given context. Ensure that the joke is appropriate, funny, and suitable for the specified cultural setting.

Culture: {t['culture']}
Context: {t['context']}

Provide the joke in plain text format. Here is an example of how your response should look:

Joke: [Your joke here]

Make sure the joke aligns with the cultural context and is not offensive."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The joke should be culturally relevant and suitable for the specified context.",
            "The joke should be appropriate and funny.",
            "The joke should not be offensive or inappropriate for the given culture and context." 
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
