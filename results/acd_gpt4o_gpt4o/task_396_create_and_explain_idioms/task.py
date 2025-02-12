class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"criteria": "Create an idiom related to the concept of perseverance."},
            "2": {"criteria": "Create a proverb that conveys the importance of teamwork."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a new idiom or proverb based on the given criteria and explain its meaning and usage.

Criteria: {t['criteria']}

Instructions:
1. Invent a new idiom or proverb that aligns with the given criteria.
2. Ensure that the idiom or proverb is original and creative.
3. Provide a detailed explanation of its meaning and how it can be used in conversation.

Your response should be in the following format:
Idiom/Proverb: [Your idiom or proverb]
Explanation: [Your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The idiom or proverb should align with the given criteria.", "The idiom or proverb should be original and creative.", "The explanation should clearly convey the meaning and usage of the idiom or proverb."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
