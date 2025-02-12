class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "Find three distinct positive integers a, b, and c such that a + b + c = 30 and a * b * c is maximized."},
            "2": {"puzzle": "Find two distinct positive integers x and y such that x^2 + y^2 = 100 and x * y is minimized."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        puzzle = t["puzzle"]
        instructions = f"""Your task is to solve the following mathematical puzzle:

Puzzle: {puzzle}

Provide your solution in the following format:
Solution: [Your solution here]
Explanation: [Your explanation here]

Make sure your solution is correct and your explanation clearly shows the steps and reasoning used to arrive at the solution. Your solution must strictly adhere to the constraints given in the puzzle. Recheck your calculations to ensure accuracy."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should be correct.",
            "The explanation should clearly show the steps and reasoning used to arrive at the solution.",
            "The solution must strictly adhere to the constraints given in the puzzle.",
            "The calculations must be accurate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
