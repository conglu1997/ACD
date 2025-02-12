class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Describe a painting of a serene landscape with mountains in the background, a river flowing through the middle, and a small cabin on the right side. Include details about the colors, lighting, and overall mood of the painting." 
            },
            "2": {
                "prompt": "Describe a modern art piece that uses geometric shapes and vibrant colors to convey a sense of chaos and energy. Include details about the arrangement of shapes, the choice of colors, and the emotions the piece evokes." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given the following prompt to describe a visual artwork:

Prompt: {t['prompt']}

Instructions:
1. Carefully read the prompt and visualize the described artwork.
2. Generate a detailed description of the artwork, including specific details about the elements mentioned in the prompt.
3. Ensure your description is vivid, coherent, and captures the essence of the visual piece accurately.
4. Submit your description as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The description should include details about the specific elements mentioned in the prompt.",
            "The description should be vivid, coherent, and capture the overall mood or emotion of the artwork.",
            "The submission should be in plain text and follow a logical flow."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
