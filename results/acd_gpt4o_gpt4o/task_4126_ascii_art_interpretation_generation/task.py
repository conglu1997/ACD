class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"ascii_art": "  *\n ***\n*****\n ***\n  *", "query": "Describe the above ASCII art in detail."},
            "2": {"description": "Create an ASCII art representation of a simple house with a door and a window."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'ascii_art' in t:
            return f"""You are given an ASCII art representation. Your task is to describe the given ASCII art in detail. The ASCII art is provided below:

{t['ascii_art']}

Your response should include a detailed description of what the ASCII art represents, focusing on its visual elements and overall structure. Provide your response in plain text format."""
        else:
            return f"""Your task is to create an ASCII art representation based on the given description.

Description: {t['description']}

Your ASCII art should be clear, coherent, and accurately represent the described scene using standard ASCII characters. Provide your ASCII art in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'ascii_art' in t:
            criteria = ["The response should accurately describe the given ASCII art.", "The description should be detailed and cover the visual elements and overall structure."]
        else:
            criteria = ["The ASCII art should accurately represent the described scene.", "The ASCII art should be clear and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
