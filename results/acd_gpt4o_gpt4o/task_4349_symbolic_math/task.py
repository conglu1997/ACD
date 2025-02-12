class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Solve the following equation for x: 2x^2 - 4x + 1 = 0."},
            "2": {"problem": "Find the derivative of the function f(x) = 3x^3 - 5x^2 + 2x - 7."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"Your task is to solve the following mathematical problem. Provide your solution in plain text format, showing all steps clearly.\n\nProblem: {t['problem']}\n\nFormat your response as follows:\nSolution: [Your step-by-step solution]\nFinal Answer: [Your final answer]"
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution should show all steps clearly.", "The final answer should be correct.", "The response should be formatted correctly as per the instructions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
