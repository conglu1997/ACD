class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"art_description": "A swirling mix of blues and greens with sharp red lines cutting through."},
            "2": {"art_description": "Geometric shapes in vibrant colors arranged asymmetrically on a black background."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret and provide a detailed description of an abstract art piece based on the given prompt.

Art Description: {t['art_description']}

Your response should include:
1. A possible interpretation of the art piece (e.g., emotions, themes, or messages it conveys).
2. A detailed visual description expanding on the given prompt, including imagined elements like texture, light, and composition.

Ensure your response is imaginative, coherent, and captures the essence of abstract art interpretation.

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The interpretation should be imaginative and coherent.",
            "The visual description should expand on the given prompt with additional details.",
            "The response should capture the essence of abstract art interpretation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
