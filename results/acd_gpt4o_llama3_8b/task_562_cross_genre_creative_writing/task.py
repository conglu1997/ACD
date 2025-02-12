class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"genre1": "science fiction", "genre2": "epic fantasy"},
            "2": {"genre1": "murder mystery", "genre2": "romantic comedy"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        genre1 = t["genre1"]
        genre2 = t["genre2"]
        return f"""Write a short story that combines elements from both {genre1} and {genre2} genres. Ensure that your story includes key themes, settings, and stylistic elements from both genres. The narrative should be engaging, coherent, and creatively blend the two genres into a seamless story. The story should be at least 500 words long. Submit your story as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should effectively blend elements from both specified genres.",
            "The narrative should be engaging and coherent.",
            "The story should include key themes, settings, and stylistic elements from both genres."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
