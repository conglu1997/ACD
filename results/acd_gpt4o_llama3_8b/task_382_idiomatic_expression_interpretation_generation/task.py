class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"expression": "Break the ice", "generation_prompt": "Create an idiom that means to start a conversation in a difficult or awkward situation."},
            "2": {"expression": "Kick the bucket", "generation_prompt": "Create an idiom that means to die."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following tasks:

1. Interpret the given idiomatic expression: '{t["expression"]}'. Provide a clear and concise explanation of its meaning.

2. Generate a new idiomatic expression based on the following criteria: {t["generation_prompt"]}. Ensure that the new idiom is creative, culturally plausible, and its meaning can be easily inferred from the context. Submit your response in the following format:

Interpretation: [Your interpretation]
New Idiom: [Your new idiom]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The interpretation of the idiom should be accurate.",
            "The new idiom should be creative and culturally plausible.",
            "The new idiom's meaning should be easily inferred from the context."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
