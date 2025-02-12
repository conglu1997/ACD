class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"work": "Romeo and Juliet", "genre": "science fiction"},
            "2": {"work": "Pride and Prejudice", "genre": "horror"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        work = t["work"]
        genre = t["genre"]
        return f"""Transform the well-known literary work '{work}' into the genre of '{genre}'. Ensure that the core narrative and characters are preserved, but the setting, style, and elements of the new genre are incorporated. Your transformation should be creative, coherent, and maintain the essence of the original story while fitting seamlessly into the new genre. Submit your transformed narrative as a plain text string in the following format:

Transformed Narrative: [Your transformed narrative here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The transformed narrative should maintain the core narrative and characters of the original work.", "The transformed narrative should incorporate elements of the specified genre.", "The transformation should be creative and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
