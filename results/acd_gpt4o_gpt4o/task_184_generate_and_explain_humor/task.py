class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Why did the chicken cross the road?"},
            "2": {"prompt": "How many programmers does it take to change a light bulb?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a joke based on the following prompt and explain why the joke is humorous:

{t["prompt"]}

Your response should include:
1. The joke.
2. An explanation of why the joke is humorous, considering any linguistic, cultural, or contextual elements that contribute to its humor.

Ensure your joke is appropriate and your explanation is clear and insightful. Your explanation should cover the structure of the joke, any wordplay or puns used, and the cultural or contextual references that make it funny. Format your response in plain text."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a joke based on the prompt.",
            "The response should include an explanation of why the joke is humorous.",
            "The joke should be appropriate and the explanation should be clear and insightful, covering the structure of the joke, any wordplay or puns used, and the cultural or contextual references that make it funny."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
