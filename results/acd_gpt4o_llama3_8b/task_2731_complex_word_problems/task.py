class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "A farmer has a certain number of chickens and cows. If the total number of heads is 50 and the total number of legs is 140, how many chickens and how many cows does the farmer have?"},
            "2": {"problem": "In a race, three athletes A, B, and C start running at the same time. A runs at a speed of 10 km/h, B at 12 km/h, and C at 15 km/h. If the race is 60 km long, how long will it take each athlete to finish the race, and who will win?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following complex word problem. Ensure that your solution includes all necessary steps and logical deductions to arrive at the correct answer.

Problem: {t['problem']}

Submit your response as a plain text string in the following format: 'Solution: [Your solution]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution should include all necessary steps and logical deductions.", "The final answer should be correct and clearly stated."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
