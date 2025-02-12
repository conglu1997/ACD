class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'emotion': 'joy', 'context': 'A reunion of old friends after many years apart.'},
            '2': {'emotion': 'sorrow', 'context': 'A character dealing with the loss of a beloved pet.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Generate a narrative that conveys a strong sense of {t['emotion']} based on the following context: {t['context']}.\nYour narrative should be vivid, emotionally charged, and immersive. It should clearly convey the specified emotion throughout the story. Submit your narrative as a plain text string."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The narrative should clearly convey the specified emotion.", "The narrative should be vivid, immersive, and emotionally charged.", "The narrative should logically follow the given context."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
