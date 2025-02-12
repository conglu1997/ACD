class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        task1 = {
            'image_context': 'Imagine a serene landscape with a clear blue sky. There is a large lake in the middle, surrounded by lush green trees. A small wooden cabin is situated on the left side of the lake, and there is a mountain range in the background.',
            'instructions': 'Generate a detailed description of the given image context. Ensure your description is vivid, coherent, and captures all the elements mentioned in the context. Submit your description as a plain text string.'
        }
        task2 = {
            'image_context': 'Imagine a bustling city street at night. There are tall buildings with neon signs, and the street is filled with people walking and cars passing by. Street vendors are selling food, and there is a sense of energy and activity in the air.',
            'instructions': 'Generate a detailed description of the given image context. Ensure your description is vivid, coherent, and captures all the elements mentioned in the context. Submit your description as a plain text string.'
        }
        return {'1': task1, '2': task2}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""{t['instructions']}\n\nImage Context:\n{t['image_context']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The description should be vivid, coherent, and capture all the elements mentioned in the context.',
            'The language used should be descriptive and contextually appropriate.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0