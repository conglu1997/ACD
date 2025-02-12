class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task": "interpret_idiom",
                "idiom": "A stitch in time saves nine."
            },
            "2": {
                "task": "create_proverb",
                "meaning": "Good things come to those who wait."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task'] == 'interpret_idiom':
            return f"Interpret the following idiomatic expression: '{t['idiom']}'. Provide a detailed explanation of its meaning and an example of a situation where it might be used. Submit your interpretation as a plain text string in the following format: 'Meaning: [Your explanation] Example: [Your example]'."
        elif t['task'] == 'create_proverb':
            return f"Create a new proverb that conveys the following meaning: '{t['meaning']}'. Ensure that the proverb is clear, memorable, and culturally appropriate. Submit your proverb as a plain text string."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task'] == 'interpret_idiom':
            validation_criteria = [
                "The explanation should accurately capture the meaning of the idiom.",
                "The example should be appropriate and illustrate the use of the idiom in context.",
                "The response should follow the format: 'Meaning: [Your explanation] Example: [Your example]'."
            ]
        elif t['task'] == 'create_proverb':
            validation_criteria = [
                "The created proverb should clearly convey the given meaning.",
                "The proverb should be clear, memorable, and culturally appropriate."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
