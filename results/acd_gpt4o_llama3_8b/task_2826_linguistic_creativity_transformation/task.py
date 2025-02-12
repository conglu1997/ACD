class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "The sun sets over the horizon, painting the sky in hues of orange and pink.", "constraint": "Transform this sentence into a haiku. A haiku consists of three lines with a syllable pattern of 5-7-5. Each line should be meaningful and contribute to the overall imagery."},
            "2": {"text": "In a quiet village, there lived a humble farmer who worked the fields from dawn till dusk.", "constraint": "Rewrite this paragraph in the style of a Shakespearean sonnet. A Shakespearean sonnet consists of 14 lines with a specific rhyme scheme: ABABCDCDEFEFGG. Each line should be written in iambic pentameter."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Transform the following text according to the specified constraint:

Text: {t['text']}

Constraint: {t['constraint']}

Submit your response in the following format:
Transformed Text: [Your transformed text here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The transformed text must adhere to the specified constraint.",
            "The transformed text must be coherent and contextually appropriate.",
            "The transformed text must maintain the original meaning or essence.",
            "The transformed text must be creative and demonstrate linguistic skill."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
