class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Solve the following integral: ∫(5x^5 - 4x^4 + 3x^3 - 2x^2 + x - 7) dx",
                "task_type": "solve"
            },
            "2": {
                "problem_prompt": "Generate a calculus problem involving integration that requires a similar level of understanding and complexity as the first task. Ensure the problem has a clear solution and provide the solution with an explanation.",
                "task_type": "generate"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "solve":
            return f"""Solve the following mathematical problem. Provide a detailed explanation of your reasoning and the final solution.

Problem:
{t['problem']}

Submit your solution as a plain text string in the following format:
'Solution: [Your solution]'
Explanation: [Your explanation]"""
        elif t["task_type"] == "generate":
            return f"""Generate a new mathematical problem involving integration. Ensure that the problem has a clear solution and requires a similar level of understanding and complexity as the first task. Provide the problem statement and the solution with an explanation.

Prompt:
{t['problem_prompt']}

Submit your response as a plain text string in the following format:
'Problem: [Your problem]'
Solution: [Your solution]'
Explanation: [Your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "solve":
            validation_criteria = ["The solution must correctly solve the integral.", "The explanation must demonstrate clear and logical mathematical reasoning."]
        elif t["task_type"] == "generate":
            validation_criteria = ["The generated problem must be of similar complexity and involve integration.", "The solution must be correct and the explanation must demonstrate clear mathematical reasoning."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
