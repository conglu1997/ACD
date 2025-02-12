import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        proverbs = [
            {
                "origin": "Chinese",
                "proverb": "The journey of a thousand miles begins with a single step.",
                "meaning": "Big accomplishments start with small beginnings.",
                "target_culture": "Native American"
            },
            {
                "origin": "African",
                "proverb": "It takes a village to raise a child.",
                "meaning": "The whole community plays a role in children's upbringing and development.",
                "target_culture": "Japanese"
            }
        ]
        return {str(i+1): proverb for i, proverb in enumerate(proverbs)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""This task involves analyzing a proverb from one culture and creating an equivalent proverb for another culture. Follow these steps:

1. Analyze the following {t['origin']} proverb: "{t['proverb']}"
2. Explain its meaning and cultural significance in 1-2 sentences.
3. Create a new proverb that conveys the same meaning but is culturally appropriate for {t['target_culture']} culture. Your new proverb should reflect the values, customs, or environment of the {t['target_culture']} culture.
4. Explain how your new proverb captures the essence of the original proverb and how it relates to {t['target_culture']} culture.

Provide your response in the following format:
Original proverb analysis: [Your analysis]
New {t['target_culture']} proverb: [Your new proverb]
Explanation: [Your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include an analysis of the {t['origin']} proverb: '{t['proverb']}'",
            f"The response should include a new proverb appropriate for {t['target_culture']} culture",
            f"The new proverb should convey a similar meaning to the original: {t['meaning']}",
            "The explanation should draw connections between the original and new proverb",
            f"The new proverb and explanation should demonstrate knowledge of {t['target_culture']} culture"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
