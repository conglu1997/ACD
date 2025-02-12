class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "pair": ["sun", "moon"],
                "example": "The sun is to the moon as..."
            },
            "2": {
                "pair": ["teacher", "student"],
                "example": "A teacher is to a student as..."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate an analogy based on the given pair of concepts. Complete the analogy in the format: '{t['example']}'. Ensure the analogy illustrates a clear and meaningful relationship between the pairs.

Examples:
1. If the pair is ["sun", "moon"], the analogy could be 'The sun is to the moon as a king is to a queen.'.
2. If the pair is ["teacher", "student"], the analogy could be 'A teacher is to a student as a captain is to a crew member.'.

Your analogy should be creative but also logical and coherent. Avoid using the examples provided in your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The analogy should be meaningful and illustrate a clear relationship between the pairs.", "The analogy should be in the correct format and coherent.", "The analogy should be creative yet logical.", "The analogy should not use the provided examples verbatim."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
