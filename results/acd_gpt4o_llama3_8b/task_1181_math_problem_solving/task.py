class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Solve the quadratic equation 2x^2 - 4x - 6 = 0. Provide a detailed explanation of each step in your solution, including how you determined the roots of the equation."
            },
            "2": {
                "problem": "Calculate the area of a triangle with sides 7, 24, and 25 using Heron's formula. Provide a detailed explanation of each step in your solution, including the calculation of the semi-perimeter and the application of Heron's formula."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following mathematical problem and provide a detailed explanation of each step involved in your solution.

Problem: {t['problem']}

Your response should include:
1. A clear and accurate solution to the problem.
2. A step-by-step explanation of the process you used to arrive at the solution, including any intermediate steps and calculations.

Example response format:
- Solution: [Your solution here]
- Explanation: [Your detailed explanation here]

Ensure your explanation is thorough and covers each step of your reasoning process. Submit your response as a plain text string in the specified format.

Note: Pay special attention to the accuracy of mathematical calculations and clarity of each step in your explanation."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The solution should be mathematically accurate.",
            "The explanation should be clear and cover each step of the reasoning process, including intermediate steps and calculations.",
            "The response should follow the specified format precisely."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
