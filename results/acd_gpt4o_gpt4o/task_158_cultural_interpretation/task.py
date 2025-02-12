class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"expression": "Break the ice", "context": "During the meeting, John tried to break the ice with a joke."},
            "2": {"expression": "Burning the midnight oil", "context": "She has been burning the midnight oil to finish her project on time."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the given cultural reference, idiom, or expression and explain its meaning in the given context.

Expression: {t['expression']}

Context: {t['context']}

Your response should include:
1. A clear and concise explanation of the expression's meaning.
2. An interpretation of how the expression applies to the provided context.

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation of the expression's meaning should be clear and accurate.",
            "The interpretation should correctly apply the expression to the provided context."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
