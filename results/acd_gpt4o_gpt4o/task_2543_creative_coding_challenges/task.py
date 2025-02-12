class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Generate a fractal pattern using a recursive function. The output should be a text-based representation of the fractal. Example: A simple representation of a Sierpinski triangle."},
            "2": {"problem": "Simulate the growth of a forest using a simple cellular automaton. The output should show the forest's state at each step. Example: Represent each tree with 'T' and empty space with '.' in a grid."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to solve the following creative coding problem:

Problem: {t['problem']}

Write a Python function to solve the problem. The function should be well-documented and include any necessary comments to explain how it works. Ensure that the output is clear and meets the requirements specified in the problem.

Provide your response in plain text format, including the full Python code and a sample output. Example:

1. Code: [Your Python code]
2. Sample Output: [Your sample output]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submission should include a well-documented Python function.",
            "The function should solve the problem as specified.",
            "The output should be clear and meet the requirements of the problem.",
            "The code should be free of syntax errors and should run correctly.",
            "The sample output should match the expected output format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
