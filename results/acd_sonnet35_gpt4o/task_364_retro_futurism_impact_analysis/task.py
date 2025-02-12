import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        historical_predictions = [
            {
                "year": 1900,
                "prediction": "By the year 2000, flying machines will be used for travel and warfare.",
                "predictor": "John Elfreth Watkins Jr.",
                "actual_outcome": "Airplanes were indeed developed and widely used for both travel and warfare by 2000."
            },
            {
                "year": 1950,
                "prediction": "By the year 2000, all energy will be solar and atomic, and fossil fuels will be a thing of the past.",
                "predictor": "Popular Mechanics magazine",
                "actual_outcome": "While solar and nuclear energy have grown, fossil fuels still play a major role in global energy production as of 2000 and beyond."
            }
        ]
        
        future_tech_domains = [
            "Artificial General Intelligence",
            "Nanotechnology",
            "Biotechnology and Genetic Engineering",
            "Quantum Computing",
            "Space Colonization"
        ]
        
        return {
            "1": random.choice(historical_predictions),
            "2": random.choice(future_tech_domains)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "year" in t:
            return f"Analyze the following historical prediction:\n\nYear: {t['year']}\nPrediction: '{t['prediction']}'\nPredictor: {t['predictor']}\nActual Outcome: {t['actual_outcome']}\n\nPlease provide your analysis in the following format:\n\n1. Historical Context (100-150 words):\nDescribe the technological and societal context at the time of the prediction.\n\n2. Prediction Analysis (150-200 words):\nAnalyze the accuracy of the prediction, discussing both correct and incorrect aspects.\n\n3. Impact Assessment (200-250 words):\nAssess the actual societal impact of the technology or concept mentioned in the prediction.\n\n4. Lessons Learned (100-150 words):\nDiscuss what can be learned from this prediction about the nature of technological forecasting and societal change."
        else:
            return f"Consider the future technology domain of {t}. Your task is to make a prediction about this technology's development and impact by the year 2050. Provide your response in the following format:\n\n1. Technology Prediction (200-250 words):\nDescribe your prediction for the state of {t} in 2050, including key capabilities and limitations.\n\n2. Development Timeline (150-200 words):\nOutline a plausible timeline for the development of this technology, including potential breakthroughs and obstacles.\n\n3. Societal Impact Assessment (250-300 words):\nAnalyze the potential positive and negative impacts of this technology on society, considering economic, ethical, and social factors.\n\n4. Policy Implications (150-200 words):\nDiscuss potential policy or regulatory measures that might be necessary to address the challenges posed by this technology.\n\n5. Uncertainty Factors (100-150 words):\nIdentify key uncertainties or potential disruptors that could significantly alter your prediction."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of historical and technological contexts.",
            "The analysis or prediction is well-reasoned and considers multiple factors and perspectives.",
            "The societal impact assessment is comprehensive and nuanced, considering both positive and negative effects.",
            "The response shows creative thinking while maintaining plausibility and scientific grounding.",
            "The writing is clear, well-structured, and effectively communicates complex ideas."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
