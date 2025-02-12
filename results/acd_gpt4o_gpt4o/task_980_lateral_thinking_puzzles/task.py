class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "A man walks into a bar and asks the bartender for a glass of water. The bartender pulls out a gun and points it at the man. The man says 'Thank you' and walks out. What happened?"},
            "2": {"puzzle": "A man is found dead in a field. He is clutching a broken matchstick. There are no signs of a struggle, and he wasn't killed by any weapon or poison. How did he die?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following lateral thinking puzzle:

Puzzle: {t['puzzle']}

Provide a detailed explanation of your solution, including the reasoning behind it. Ensure that your explanation is clear, logically coherent, and addresses the puzzle adequately. Your response should be in plain text format.

Format your response as follows:

Solution: <your detailed explanation>"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        # Define criteria for evaluation
        criteria = [
            "The explanation should be clear and logically coherent.",
            "The solution should adequately address the puzzle and provide a plausible explanation.",
            "The explanation should not be self-contradictory.",
            "The solution should not rely on information not provided in the puzzle.",
            "The solution should be creative and demonstrate lateral thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
