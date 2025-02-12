class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Find the derivative of the function f(x) = 3x^4 - 5x^3 + 2x - 7."},
            "2": {"problem": "Evaluate the integral of the function g(x) = x^3 - 4x + 6 from x = 0 to x = 2."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following calculus problem:

Problem:
{t['problem']}

Provide your solution in the form of a detailed step-by-step explanation and the final answer. Format your response as follows:

Step-by-Step Solution:
1. [First step]
2. [Second step]
...
Final Answer: [Your final answer]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution must include a detailed step-by-step explanation.",
            "Each step in the solution must be correct and logically consistent.",
            "The final answer must be correct."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
