class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"sentence": "The old man the boats."},
            "2": {"sentence": "I saw the man with the telescope."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the given sentence and provide explanations for each possible interpretation. Make sure to explain the different meanings clearly and provide examples if necessary. Here is the sentence:\n\nSentence: {t['sentence']}\n\nSubmit your interpretations in plain text format, with each interpretation clearly separated.\n\nExample format:\n\nInterpretation 1: <explanation>\nInterpretation 2: <explanation>\n..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include multiple interpretations of the sentence.",
            "Each interpretation should be clearly explained.",
            "The explanations should be accurate and reflect the different possible meanings of the sentence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
