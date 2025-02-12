class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"instruction": "Describe the pattern formed by the following sequence of shapes: Circle, Square, Circle, Square, Triangle, Circle, Square, Circle. Then, predict the next two shapes in the sequence. Provide your response in the following format:\nPattern Description: [Your description]\nNext Shapes: [Next shape 1], [Next shape 2]"},
            "2": {"instruction": "Imagine a 3x3 grid. Place the following symbols in the grid based on their descriptions: 'X' in the center, 'O' in the top-left corner, '#' in the bottom-right corner, '*' in the top-right corner, and '@' in the bottom-left corner. Describe the final arrangement of the grid. Provide your response in the following format:\nGrid Description: [Your description]"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to interpret and generate visual patterns or descriptions based on spatial constraints. Read the instructions carefully and provide your response in plain text format.

Instruction: {t['instruction']}"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately describe the visual pattern or arrangement.",
            "The response should correctly predict or complete the sequence or grid based on the given instructions.",
            "The response should follow the specified format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
