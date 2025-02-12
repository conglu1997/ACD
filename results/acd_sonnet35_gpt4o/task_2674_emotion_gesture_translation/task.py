class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "emotion": "pride",
                "source_culture": "Japanese",
                "target_culture": "Brazilian"
            },
            "2": {
                "gesture": "touching one's ear",
                "source_culture": "Italian",
                "target_culture": "Indian"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "emotion" in t:
            return f"""Translate the emotion of {t['emotion']} from {t['source_culture']} culture to an equivalent physical gesture in {t['target_culture']} culture. Your response should include:

            1. A brief description of how {t['emotion']} is typically expressed non-verbally in {t['source_culture']} culture (2-3 sentences).
            2. An equivalent physical gesture that would convey a similar emotional meaning in {t['target_culture']} culture (2-3 sentences).
            3. An explanation of the cultural factors influencing the difference in expression between the two cultures (3-4 sentences).
            4. Potential misunderstandings that could arise if the gesture from one culture were used in the other, and how to avoid them (2-3 sentences).

            Ensure your response is culturally sensitive and based on general cultural tendencies, acknowledging that individual expressions may vary.
            """
        else:
            return f"""Interpret the gesture of {t['gesture']} from {t['source_culture']} culture and translate it to an equivalent emotional state or meaning in {t['target_culture']} culture. Your response should include:

            1. The typical meaning or emotional state associated with {t['gesture']} in {t['source_culture']} culture (2-3 sentences).
            2. An equivalent emotional state or meaning in {t['target_culture']} culture, and how it might be expressed non-verbally (2-3 sentences).
            3. An explanation of the cultural factors influencing the difference in interpretation between the two cultures (3-4 sentences).
            4. Potential misunderstandings that could arise if the gesture were used in the target culture, and how to avoid them (2-3 sentences).

            Ensure your response is culturally sensitive and based on general cultural tendencies, acknowledging that individual interpretations may vary.
            """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all four required points.",
            "The explanation demonstrates a nuanced understanding of both cultures.",
            "The translation of emotion/gesture is plausible and culturally appropriate.",
            "The response shows sensitivity to cultural differences and potential misunderstandings.",
            "The explanation of cultural factors is insightful and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
