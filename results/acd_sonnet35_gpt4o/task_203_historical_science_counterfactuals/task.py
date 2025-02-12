import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "historical_event": "The Library of Alexandria was never destroyed",
                "affected_field": "Mathematics and Astronomy",
                "time_period": "Classical Antiquity to Early Middle Ages"
            },
            {
                "historical_event": "The Black Death never occurred in Europe",
                "affected_field": "Medicine and Public Health",
                "time_period": "Late Middle Ages to Early Renaissance"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Analyze the following historical counterfactual scenario:\n\n" + \
               f"Historical Event: {t['historical_event']}\n" + \
               f"Affected Field: {t['affected_field']}\n" + \
               f"Time Period: {t['time_period']}\n\n" + \
               "Your task is to:\n\n" + \
               "1. Historical Analysis (150-200 words):\n" + \
               "   - Briefly describe the actual historical event and its known impacts\n" + \
               "   - Explain the immediate consequences if the event had not occurred as stated\n\n" + \
               "2. Scientific Development (200-250 words):\n" + \
               "   - Analyze how the altered historical outcome would have affected scientific progress in the specified field\n" + \
               "   - Discuss at least two specific areas of scientific knowledge that would have developed differently\n" + \
               "   - Consider both positive and negative effects on scientific advancement\n\n" + \
               "3. Technological Innovation (200-250 words):\n" + \
               "   - Propose a plausible technological innovation that could have resulted from this alternative history\n" + \
               "   - Describe the proposed technology's function, underlying scientific principles, and potential applications\n" + \
               "   - Explain how this technology connects to the altered historical event and subsequent scientific developments\n\n" + \
               "4. Broader Implications (150-200 words):\n" + \
               "   - Discuss how this alternative historical path and resulting technology might have influenced society, culture, or other scientific fields\n" + \
               "   - Consider potential ethical implications or challenges that might arise from this alternate timeline\n\n" + \
               "Ensure your response demonstrates a deep understanding of historical events, scientific principles, and technological development. Use clear, logical reasoning to connect your counterfactual scenario to plausible scientific and technological outcomes."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of the historical event and its actual impacts",
            "The analysis of altered scientific development is logically consistent and well-reasoned",
            "The proposed technological innovation is plausible and clearly connected to the alternative historical outcome",
            "The broader implications are thoughtfully considered and demonstrate an understanding of the interconnectedness of history, science, and society",
            "The response shows creativity and original thinking while remaining grounded in historical and scientific facts"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
