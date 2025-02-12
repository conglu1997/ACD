class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "original_sentence": "The quick brown fox jumps over the lazy dog."
            },
            "2": {
                "original_sentence": "Actions speak louder than words."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Rephrase the following sentence to convey the same meaning using different words and structures:

Original sentence: '{t['original_sentence']}'

Ensure that the rephrased sentence retains the original meaning and is grammatically correct. Avoid trivial rephrasing such as simple synonym replacement without restructuring the sentence. Submit your response as a plain text string in the format: 'Rephrased sentence: [Your sentence]'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The rephrased sentence must retain the original meaning.",
            "The rephrased sentence must be grammatically correct.",
            "The rephrased sentence must use different words and structure.",
            "The rephrased sentence should not be a trivial rephrasing."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
