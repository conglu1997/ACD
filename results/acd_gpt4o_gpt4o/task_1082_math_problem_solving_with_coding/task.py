class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Find the greatest common divisor (GCD) of two integers using the Euclidean algorithm."
            },
            "2": {
                "problem": "Implement a function to find the nth Fibonacci number using an efficient algorithm." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        instructions = f"""Your task is to solve the following mathematical problem by writing a Python function and then explain your solution:

Problem: {problem}

Provide your solution in two parts:
1. The Python function to solve the problem.
2. A detailed explanation of how your function works and why it solves the problem correctly.

Ensure that your code is correct, efficient, and follows best practices. Your explanation should be in plain text format, clear, concise, and demonstrate your understanding of both the problem and the solution.

Your response should be formatted as follows:
Python Function:
[your function here]

Explanation:
[your explanation here]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The Python function should correctly solve the problem.",
            "The explanation should clearly describe how the function works and why it solves the problem.",
            "The code should be efficient and follow best practices.",
            "The explanation should be in plain text format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
