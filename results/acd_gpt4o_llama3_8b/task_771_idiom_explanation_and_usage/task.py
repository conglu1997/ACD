class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "idiom": "Break the ice",
                "instructions": "Explain the meaning of the idiom 'Break the ice' and use it in a sentence. Your explanation should be clear and accurate, and the sentence should correctly illustrate the idiom's meaning. Submit your response as a plain text string."
            },
            "2": {
                "idiom": "Bite the bullet",
                "instructions": "Explain the meaning of the idiom 'Bite the bullet' and use it in a sentence. Your explanation should be clear and accurate, and the sentence should correctly illustrate the idiom's meaning. Submit your response as a plain text string."
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
            "The explanation of the idiom should be clear and accurate.",
            "The sentence should correctly illustrate the idiom's meaning."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
