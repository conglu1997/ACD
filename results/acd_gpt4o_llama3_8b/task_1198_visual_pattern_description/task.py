class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Imagine a pattern consisting of concentric circles with alternating colors of red and blue. The smallest circle has a radius of 1 cm, and each subsequent circle increases in radius by 1 cm. Describe this pattern in detail, including the size and spacing of the circles."},
            "2": {"description": "Imagine a pattern made up of triangles and squares arranged in a checkerboard fashion. The triangles are green, and the squares are yellow. Each shape has a side length of 2 cm. Describe this pattern in detail, including the size and arrangement of the shapes."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t['description']
        return f"""Read the following description of an imaginary visual pattern and provide a detailed textual description of the pattern. Ensure that your description includes specific details about the size, color, and arrangement of the elements in the pattern.

Description: {description}

Submit your response as a plain text string in the following format:

Pattern Description: [Your detailed description]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should accurately represent the visual pattern described in the prompt.",
            "The description should be detailed and include specific information about the size, color, and arrangement of the elements.",
            "The language used should be clear and unambiguous."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
