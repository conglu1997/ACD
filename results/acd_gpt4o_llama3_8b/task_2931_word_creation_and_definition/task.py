class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "constraints": "The word must start with the letter 'Z', be at least 8 characters long, and relate to technology.",
                "example": "Zynaptic: An advanced neural interface technology that allows direct communication between the human brain and computers."
            },
            "2": {
                "constraints": "The word must end with the suffix '-ology', be at least 10 characters long, and describe a new scientific field.",
                "example": "Neurosonology: The study of the effects of sound waves on neural activity and brain function."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a new word based on the following constraints and provide its definition. Ensure that the word is plausible, adheres to the constraints, and its definition is coherent and meaningful. Avoid using any existing words or direct hints.

Constraints: {t['constraints']}

Example: {t['example']}

Submit your response in the following format:

Word: [Your new word here]
Definition: [The definition of your new word]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The new word must adhere to the given constraints.",
            "The definition must be coherent and meaningful.",
            "The word must be plausible and not an existing word."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
