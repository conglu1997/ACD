class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"input_text": "The quick brown fox jumps over the lazy dog on a sunny day in the forest.", "target_style": "Shakespearean English"},
            "2": {"input_text": "A stitch in time saves nine, preventing greater troubles ahead.", "target_style": "Modern English"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to transform the following text into the specified linguistic style:

Input Text: {t['input_text']}
Target Style: {t['target_style']}

Provide your transformation in plain text format, ensuring it accurately reflects the target linguistic style while retaining the original meaning. The transformed text should be between 30 to 100 words. Start your transformation with 'Transformed Text: ' to indicate the beginning of your response.

Example Transformation:
Input Text: 'Friends, Romans, countrymen, lend me your ears.'
Target Style: Modern English
Transformed Text: 'Hello everyone, please listen to what I have to say.'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The submission should start with 'Transformed Text: '", "The transformed text should be between 30 to 100 words.", "The submission should accurately reflect the target linguistic style.", "The transformation should retain the original meaning of the text."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
