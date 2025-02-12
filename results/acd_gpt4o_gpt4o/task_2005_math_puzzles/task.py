class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"parameters": "Generate a 4x4 magic square with unique integers from 1 to 16."},
            "2": {"parameters": "Solve the following system of linear equations: 2x + 3y = 6, 4x - y = 2."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        parameters = t["parameters"]
        return f"""Your task is to solve the following mathematical puzzle based on the given parameters. Ensure that your solution is accurate, logical, and clearly explained. Provide your response in plain text format.

Parameters: {parameters}

Provide your solution in the following format:
1. Explanation of the approach
2. Step-by-step solution
3. Final answer"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
