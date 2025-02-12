class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Describe a small cozy living room. Include details about the furniture, colors, decorations, lighting, and overall ambiance."},
            "2": {"prompt": "Interpret the following description and generate a labeled diagram based on it: 'A circular garden with a fountain at the center, surrounded by four flower beds, each with a different type of flower. A stone path runs around the fountain and connects the flower beds. There is a bench near one of the flower beds.'"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves generating and interpreting detailed physical descriptions based on the given prompts:\n\nPrompt: {t['prompt']}\n\nFor Task 1: Generate a detailed description of the specified environment, including information about the furniture, colors, decorations, lighting, and overall ambiance.\nFor Task 2: Interpret the provided description and generate a labeled diagram based on it. Ensure the diagram accurately represents the spatial relationships and components mentioned in the description. Submit your response in the following format:\n- Diagram Description: [A detailed text description of the diagram components and their spatial relationships]\n- Labels: [List of labels for different components as mentioned in the description]\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description in Task 1 should be detailed, coherent, and include information about the furniture, colors, decorations, lighting, and overall ambiance.",
            "The diagram description in Task 2 should accurately reflect the spatial relationships and components mentioned in the description and be clearly labeled."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
