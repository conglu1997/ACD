class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Solve the following arithmetic problem: (58 + 67 - 32) * 5 / 4 + 12 - 7 * 3 + 1"
            },
            "2": {
                "problem": "Solve the following algebraic equation for x: 2x^2 - 3x + 5 = x^2 - 7 + 4x"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following mathematical problem. Provide a step-by-step solution and the final answer in the format specified below. Here is the problem:

{t["problem"]}

Ensure your solution is accurate and clearly shows each step. Submit your solution as a plain text string in the following format:

Step-by-Step Solution:
[Your step-by-step solution here]

Final Answer:
[Your final answer here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should include a step-by-step solution.",
            "The final answer should be correct.",
            "The solution steps should be logically valid and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
