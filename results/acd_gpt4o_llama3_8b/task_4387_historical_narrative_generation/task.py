class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "historical_event": "The fall of the Berlin Wall in 1989",
                "cultural_setting": "A family reunion in East Berlin during the initial opening of the border crossings"
            },
            "2": {
                "historical_event": "The signing of the Treaty of Versailles in 1919",
                "cultural_setting": "A discussion among French citizens in a Parisian café about the implications of the treaty"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        historical_event = t['historical_event']
        cultural_setting = t['cultural_setting']
        return f"""Generate a detailed and contextually accurate narrative based on the following historical event and cultural setting:

Historical Event: {historical_event}
Cultural Setting: {cultural_setting}

Ensure that your narrative captures the historical context, cultural nuances, and the emotions of the characters involved. Your narrative should:
1. Be approximately 300-400 words long.
2. Include specific references to the historical event and cultural setting.
3. Provide authentic details that reflect the time period and cultural background.
4. Quote or reference actual historical details or events to enhance authenticity.

Submit your response as a plain text string in the following format:

Narrative:
[Your narrative here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The narrative should be historically accurate.",
            "The narrative should capture the cultural nuances of the setting.",
            "The narrative should be emotionally engaging and coherent.",
            "The narrative should be approximately 300-400 words long.",
            "The narrative should include authentic details that reflect the time period and cultural background.",
            "The narrative should quote or reference actual historical details or events."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
