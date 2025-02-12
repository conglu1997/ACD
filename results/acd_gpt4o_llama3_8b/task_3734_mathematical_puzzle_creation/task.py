class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "type": "number_sequence",
                "constraints": "Create a number sequence puzzle where the next number in the sequence is determined by a unique mathematical pattern. Provide the first 5 numbers in the sequence and describe the pattern."
            },
            "2": {
                "type": "grid_puzzle",
                "constraints": "Create a 4x4 grid puzzle where each cell contains a number. The puzzle should have a unique solution based on given mathematical rules. Provide the initial grid with some numbers filled in and describe the rules for solving the puzzle."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "number_sequence":
            return f"""Create a number sequence puzzle based on the following constraints:\n\n{t['constraints']}\n\nExample Format:\n1. First 5 numbers in the sequence: [2, 4, 8, 16, 32]\n2. Pattern description: 'Each number is the previous number multiplied by 2.'\n\nSubmit your response as a plain text string in the following format:\n1. First 5 numbers in the sequence: [number1, number2, number3, number4, number5]\n2. Pattern description: [description of the pattern]"""
        elif t["type"] == "grid_puzzle":
            return f"""Create a 4x4 grid puzzle based on the following constraints:\n\n{t['constraints']}\n\nExample Format:\n1. Initial grid: [[1, 0, 0, 4], [0, 3, 0, 0], [0, 0, 2, 0], [4, 0, 0, 1]]\n2. Rules: 'Each row and column must contain the numbers 1 to 4 without repetition.'\n\nSubmit your response as a plain text string in the following format:\n1. Initial grid: [initial grid with some numbers filled in]\n2. Rules: [description of the rules for solving the puzzle]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "number_sequence":
            criteria = [
                "The sequence should follow a unique and logical mathematical pattern.",
                "The pattern should be clearly described and should logically generate the sequence provided.",
                "The pattern should not be trivial or overly simple (e.g., adding 1 each time)."
            ]
        elif t["type"] == "grid_puzzle":
            criteria = [
                "The initial grid should be a valid 4x4 grid with some numbers filled in.",
                "The rules should be clear, logical, and lead to a unique solution for the puzzle.",
                "The puzzle should not be trivially solvable (e.g., leaving only one cell empty)."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
