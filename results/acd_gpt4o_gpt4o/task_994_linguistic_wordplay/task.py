class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "What do you call fake spaghetti?"},
            "2": {"puzzle": "Why don’t scientists trust atoms?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following linguistic puzzle involving wordplay or a pun. Given the puzzle: '{t["puzzle"]}', provide a clever and humorous answer that fits the wordplay or pun.

Ensure that your answer is concise, witty, and demonstrates an understanding of the language nuances involved in the puzzle. Provide your answer in the format: Answer: <your answer>"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should provide a clever and humorous answer that fits the wordplay or pun.",
            "The answer should be concise and demonstrate an understanding of the language nuances involved in the puzzle.",
            "The answer should be provided in the format: Answer: <your answer>"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
