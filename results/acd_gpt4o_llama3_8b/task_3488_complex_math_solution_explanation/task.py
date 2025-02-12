class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Solve the following integral and provide a detailed explanation of the solution steps: ∫(x^3 * e^x) dx"
            },
            "2": {
                "problem": "Solve the following differential equation and provide a detailed explanation of the solution steps: y'' + 3y' + 2y = e^x"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following mathematical problem and provide a detailed explanation of each step involved in reaching the solution:

Problem: {t['problem']}

Ensure that your solution includes:
1. A clear statement of the problem.
2. Step-by-step solution process with justifications for each step.
3. The final answer with appropriate units or notation.

Submit your response as a plain text string in the following format:

1. Problem Statement: [Restate the problem]
2. Solution Steps: [Provide detailed steps with explanations and justifications]
3. Final Answer: [Provide the final answer clearly]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The submission should include a clear restatement of the problem.", "The solution should include detailed, logical steps with justifications for each step.", "The final answer should be correct and appropriately notated."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
