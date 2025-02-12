class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"parameters": "Create a number-based puzzle that involves a sequence with a hidden pattern. The sequence should have at least 5 numbers. Provide a solution to the puzzle, including the pattern and the next number in the sequence."},
            "2": {"parameters": "Create a geometry-based puzzle that involves identifying a hidden shape within a larger figure. The larger figure should be composed of at least 5 different shapes. Provide a solution to the puzzle, including the identification and explanation of the hidden shape."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a mathematical puzzle based on the given parameters and then provide a solution to the puzzle. Here are the parameters: '{t["parameters"]}'.

Your response should be in the following format:

1. Puzzle: [description of the puzzle]
2. Solution: [detailed solution to the puzzle]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The puzzle should be logically coherent and adhere to the given parameters.",
            "The solution should accurately and clearly solve the puzzle.",
            "The puzzle and solution should be original and creative.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
