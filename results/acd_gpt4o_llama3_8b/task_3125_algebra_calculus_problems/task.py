class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Solve the following quadratic equation for x and show all steps: 3x^2 - 12x + 9 = 0"},
            "2": {"problem": "Evaluate the following definite integral and show all steps: ∫(2x^3 - 5x^2 + 4x - 1) dx from x=1 to x=3"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        return f"""Solve the following problem and provide a detailed, step-by-step solution:

Problem: {problem}

Your response should include all intermediate steps and the final answer. Submit your response as a plain text string in the following format:

Solution:
Step 1: [First step]
Step 2: [Second step]
...
Final Answer: [Your final answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include all intermediate steps and the final answer should be correct.", "The solution should be logically consistent and each step should follow from the previous one.", "All necessary mathematical notation and operations should be used correctly.", "The final answer should be clearly indicated."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
