class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "nature", "word_list": ["tree", "leaf", "wind", "river", "mountain"]},
            "2": {"theme": "love", "word_list": ["heart", "kiss", "together", "forever", "dream"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        word_list = t["word_list"]
        return f"""Create a visual poem based on the theme '{theme}'. Use the following words in your poem: {', '.join(word_list)}. Arrange the words in a visually appealing and meaningful format that reflects the theme. Your poem should be creative, aesthetically pleasing, and convey a coherent idea related to the theme. Submit your visual poem as a plain text string. Describe the visual arrangement using spaces, new lines, and indentation as needed to illustrate the format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The poem should be visually appealing.",
            "The poem should use all the provided words.",
            "The poem should convey a coherent idea related to the theme.",
            "The poem should be creative and reflect the theme accurately."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
