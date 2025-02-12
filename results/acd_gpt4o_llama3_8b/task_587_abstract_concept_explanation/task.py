class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "instructions": "Explain the concept of 'Justice' in a clear and understandable manner. Your explanation should include: 1. A definition of the concept. 2. A brief discussion of its significance. 3. At least two examples that illustrate the concept in different contexts. Submit your response as a plain text string."
            },
            "2": {
                "instructions": "Explain the concept of 'Entropy' in a clear and understandable manner. Your explanation should include: 1. A definition of the concept. 2. A brief discussion of its significance in physics and information theory. 3. At least two examples that illustrate the concept in different contexts. Submit your response as a plain text string."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return t["instructions"]

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should include a clear and accurate definition of the concept.",
            "The explanation should discuss the significance of the concept.",
            "The examples should be relevant and illustrate the concept in different contexts."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
