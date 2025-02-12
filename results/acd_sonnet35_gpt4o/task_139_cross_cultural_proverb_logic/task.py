class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        import random
        proverbs = [
            {
                "proverb": "The early bird catches the worm.",
                "culture": "English",
                "logic": "Those who act first gain an advantage."
            },
            {
                "proverb": "The nail that sticks out gets hammered down.",
                "culture": "Japanese",
                "logic": "Nonconformity leads to negative consequences."
            },
            {
                "proverb": "A rolling stone gathers no moss.",
                "culture": "Latin",
                "logic": "Constant movement or change prevents stagnation."
            }
        ]
        tasks = random.sample(proverbs, 2)
        return {
            "1": tasks[0],
            "2": tasks[1]
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following proverb from {t['culture']} culture: "{t['proverb']}"

        Your task is to:
        1. Identify the underlying logical structure of the proverb (2-3 sentences, about 30-50 words).
        2. Create a new proverb that maintains the same logical structure but is adapted to a different cultural context of your choice. The new culture should be significantly different from the original.
        3. Explain how your new proverb maintains the original logical structure and how it reflects the new cultural context (3-4 sentences, about 50-75 words).

        Provide your response in the following format:

        Original Proverb: [Repeat the given proverb]
        Logical Structure: [Your analysis of the logical structure]
        New Culture: [Name of the new culture you've chosen]
        New Proverb: [Your newly created proverb]
        Explanation: [Your explanation of how the new proverb maintains the logical structure and reflects the new culture]
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response correctly identifies the logical structure of the original proverb, capturing its essence in 2-3 sentences (30-50 words).",
            "The new proverb maintains the same logical structure as the original, demonstrating a clear parallel in reasoning.",
            "The new proverb is adapted to a significantly different cultural context, showing understanding of diverse cultural elements.",
            "The explanation (3-4 sentences, 50-75 words) clearly shows how the new proverb maintains the original logic and reflects the new culture.",
            "The response is well-structured and follows the requested format exactly."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
