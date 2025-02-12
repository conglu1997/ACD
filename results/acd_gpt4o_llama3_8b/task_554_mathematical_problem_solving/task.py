class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Solve the following equation for x: 3x + 5 = 20. Show all steps in your solution."
            },
            "2": {
                "problem": "Calculate the roots of the quadratic equation: x^2 - 4x + 4 = 0. Show all steps in your solution."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following mathematical problem and provide a clear explanation for your solution:

Problem:
{t['problem']}

Ensure that your explanation is detailed, logical, and easy to understand. Show all steps in your solution. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The solution should be correct.",
            "The explanation should be detailed and logical.",
            "The response should be clear and easy to understand.",
            "All steps in the solution should be shown."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
