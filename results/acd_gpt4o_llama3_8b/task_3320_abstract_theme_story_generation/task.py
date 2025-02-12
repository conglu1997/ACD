class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "Time",
                "task": "Generate a short story based on the abstract theme of 'Time'. Your story should creatively explore the concept and capture its essence. Aim for a length of 300-500 words."
            },
            "2": {
                "theme": "Freedom",
                "task": "Generate a short story based on the abstract theme of 'Freedom'. Your story should creatively explore the concept and capture its essence. Aim for a length of 300-500 words."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are required to generate a short story based on the given abstract theme. Your story should creatively explore the concept and capture its essence. Aim for a length of 300-500 words.

Theme: {t['theme']}

Task: {t['task']}

Submit your response as a plain text string in the following format:

Story: [Your story]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The story should creatively explore the given abstract theme.",
            "The story should capture the essence of the theme.",
            "The story should be coherent and engaging.",
            "The story should be within the specified length of 300-500 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
