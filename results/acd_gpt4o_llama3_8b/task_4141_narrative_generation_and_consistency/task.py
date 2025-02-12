class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"genre": "science fiction", "characters": ["robot", "human"], "setting": "space station"},
            "2": {"genre": "fantasy", "characters": ["wizard", "dragon"], "setting": "ancient forest"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        genre = t["genre"]
        characters = ', '.join(t["characters"])
        setting = t["setting"]
        return f"""Generate a fictional story based on the following constraints:\nGenre: {genre}\nCharacters: {characters}\nSetting: {setting}\n\nYour story should be engaging and coherent, with a clear plot that includes a beginning, middle, and end. The story should develop the characters and their motivations, and the setting should influence the plot. Once you have generated the story, answer the following questions to ensure logical consistency:\n1. What motivates each character?\n2. How does the setting influence the plot?\n3. Identify any logical inconsistencies in the story and correct them.\n\nSubmit your response as a plain text string in the following format:\nStory: [Your story here]\nCharacter Motivations: [Character motivations here]\nSetting Influence: [Setting influence here]\nLogical Inconsistencies: [Logical inconsistencies and corrections here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should adhere to the given genre, characters, and setting.",
            "The story should be engaging and coherent with a clear beginning, middle, and end.",
            "The character motivations should be logically consistent with their actions.",
            "The setting should have a clear influence on the plot.",
            "All identified logical inconsistencies should be addressed and corrected." ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
