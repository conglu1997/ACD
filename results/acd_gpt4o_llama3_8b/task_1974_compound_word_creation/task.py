class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "components": ["sun", "flower"],
                "description": "Combine the given components to create a compound word or phrase. Provide a detailed explanation of the meaning of the resulting compound word or phrase and use it in a sentence."
            },
            "2": {
                "components": ["moon", "light"],
                "description": "Combine the given components to create a compound word or phrase. Provide a detailed explanation of the meaning of the resulting compound word or phrase and use it in a sentence."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Combine the given components to create a compound word or phrase. Provide a detailed explanation of the meaning of the resulting compound word or phrase and use it in a sentence. Ensure that your explanation is detailed and logically structured. Submit your response as a plain text string in the following format:\n\nCompound Word: [Your compound word or phrase]\nMeaning: [Your detailed explanation of the meaning]\nSentence: [A sentence using the compound word or phrase]\n\nComponents: {', '.join(t['components'])}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The compound word or phrase should be a logical combination of the given components.",
            "The explanation should accurately describe the meaning of the resulting compound word or phrase.",
            "The sentence should use the compound word or phrase correctly."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
