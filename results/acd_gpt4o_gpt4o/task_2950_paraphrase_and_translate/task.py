class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "The quick brown fox jumps over the lazy dog.", "task": "paraphrase"},
            "2": {"text": "Life is what happens when you're busy making other plans.", "task": "translate", "language": "Spanish"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task'] == "paraphrase":
            instructions = f"""Your task is to paraphrase the following text:

{t['text']}

Ensure that the paraphrased text conveys the same meaning as the original but uses different words and phrases. The paraphrased text should be coherent and maintain the original intent. Provide your response in plain text format."""
        else:
            instructions = f"""Your task is to translate the following text into {t['language']}:

{t['text']}

Ensure that the translation preserves the original meaning and is grammatically correct in the target language. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t['task'] == "paraphrase":
            criteria.append("The paraphrased text should convey the same meaning as the original.")
            criteria.append("The paraphrased text should use different words and phrases.")
            criteria.append("The paraphrased text should be coherent and maintain the original intent.")
        else:
            criteria.append("The translation should preserve the original meaning.")
            criteria.append("The translation should be grammatically correct in the target language.")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
