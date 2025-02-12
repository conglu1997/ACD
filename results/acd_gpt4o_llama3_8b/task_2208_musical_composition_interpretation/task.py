class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "composition": "C E G B A F D C E G B D A F"
            },
            "2": {
                "composition": "A C E G B D F A E C D G B F"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the given short musical composition and describe the emotions, imagery, or story it conveys. The composition is represented by a sequence of notes. Your interpretation should be vivid, imaginative, and capture the essence of the music. Ensure your interpretation is at least 200 words long. Submit your response as a plain text string.

Composition: {t['composition']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The interpretation should be vivid and imaginative.",
            "The interpretation should capture the essence of the music.",
            "The interpretation should be coherent and expressive.",
            "The interpretation should be at least 200 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
