class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "A swirl of vibrant colors, with no distinct shapes or figures. The colors blend and clash, creating a sense of chaos and energy. In the center, a small, calm blue circle stands out amidst the turmoil." 
            },
            "2": {
                "description": "An intricate pattern of geometric shapes in varying shades of gray. Some shapes are sharp and angular, while others are smooth and curved. The overall composition is balanced, yet mysterious, as if hiding a deeper meaning." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a creative story based on the following description of an abstract art piece:

Description: {t['description']}

Your story should be at least 500 words long, include well-developed characters, a coherent plot, and an engaging narrative. The story should capture the essence of the abstract art description and reflect its mood and themes. Ensure your story is imaginative, provides a unique interpretation of the art piece, and follows a clear structure with a beginning, middle, and end. Submit your story as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should be at least 500 words long.",
            "The story should include well-developed characters and a coherent plot.",
            "The story should capture the essence of the abstract art description.",
            "The story should be engaging and reflect the mood and themes of the art.",
            "The story should be imaginative, provide a unique interpretation of the art piece, and follow a clear structure with a beginning, middle, and end."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
