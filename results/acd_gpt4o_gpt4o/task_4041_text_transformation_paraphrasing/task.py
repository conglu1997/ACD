class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"original_text": "The quick brown fox jumps over the lazy dog.", "transformation": "Rewrite the sentence in a more formal and professional tone while keeping the essence of the original meaning."},
            "2": {"original_text": "She sells seashells by the seashore.", "transformation": "Convert this tongue twister into a short rhyming poem of at least four lines that maintains the playful nature of the original."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to transform the given text according to the specified transformation. Here is the text and the transformation requirement:

Original Text: {t['original_text']}
Transformation Requirement: {t['transformation']}

Provide a detailed response that adheres to the transformation requirement. Ensure that your response maintains the meaning, coherence, and flow of the original text while fulfilling the transformation criteria. Provide your response in plain text format as follows:

Transformed Text: [Your transformed text here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The transformed text should maintain the meaning of the original text.",
            "The transformation should adhere to the specified requirement (e.g., change of tone, poetic form).",
            "The transformed text should maintain coherence and flow.",
            "The transformed text should specifically match the given transformation requirement."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
