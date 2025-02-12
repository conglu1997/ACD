class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "A train leaves Station A at 9:00 AM and travels to Station B at an average speed of 60 km/h. Two hours later, another train leaves Station B and travels to Station A at an average speed of 80 km/h. If the distance between the two stations is 300 km, at what time will the two trains meet?"},
            "2": {"prompt": "A farmer has a rectangular field that is 20 meters longer than it is wide. If the perimeter of the field is 400 meters, what are the dimensions of the field?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following mathematical word problem and explain the solution process step-by-step:\n\nPrompt: {t['prompt']}\n\nProvide a clear and detailed explanation of each step involved in solving the problem. Ensure that your solution is logically sound and accurately addresses the problem.\n\nFormat your response as follows:\n1. Explanation: [Step-by-step explanation]\n2. Answer: [Final answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The step-by-step explanation should be clear, logical, and complete.",
            "The final answer should be correct based on the given problem.",
            "The response format should match the specified format: Explanation followed by Answer."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
