import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "language": "English",
                "time_period": "2023 to 2123",
                "linguistic_aspect": "Syntax",
                "social_factor": "Technological advancements"
            },
            {
                "language": "Mandarin Chinese",
                "time_period": "2023 to 2123",
                "linguistic_aspect": "Phonology",
                "social_factor": "Globalization"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""
        Analyze historical language evolution patterns in {t['language']} and use them to predict future changes from {t['time_period']}, focusing on {t['linguistic_aspect']} and considering the social factor of {t['social_factor']}. Then, design an AI system to model and forecast these changes. Your response should include:

        1. Historical Analysis (250-300 words):
           a) Briefly outline the major changes in {t['linguistic_aspect']} that {t['language']} has undergone in the past 500 years.
           b) Identify key patterns or trends in these changes.
           c) Discuss how {t['social_factor']} has influenced these changes historically.

        2. Future Prediction (300-350 words):
           a) Based on historical patterns, predict three specific changes in {t['linguistic_aspect']} that {t['language']} might undergo from {t['time_period']}.
           b) Explain the reasoning behind each prediction, linking it to historical trends and the influence of {t['social_factor']}.
           c) Discuss any potential challenges or limitations in making these predictions.

        3. AI System Design (300-350 words):
           a) Propose an AI system architecture for modeling and forecasting the language changes you predicted.
           b) Explain how your system would incorporate historical data, current linguistic theories, and the influence of {t['social_factor']}.
           c) Describe any novel algorithms or techniques your system would use to improve its predictive accuracy.
           d) Discuss how your system would handle uncertainty and variability in language evolution.

        4. Validation and Testing (200-250 words):
           a) Propose a method to validate the accuracy of your AI system's predictions.
           b) Describe an experiment to test the influence of {t['social_factor']} on your model's forecasts.
           c) Discuss the challenges in testing and validating models of long-term language evolution.

        5. Ethical and Societal Implications (200-250 words):
           a) Discuss potential ethical concerns related to predicting and potentially influencing language evolution.
           b) Analyze how accurate predictions of language change might impact society, education, and technology.
           c) Propose guidelines for the responsible use of such AI systems in linguistics and language policy.

        6. Interdisciplinary Connections (150-200 words):
           a) Explain how your approach integrates knowledge from linguistics, cognitive science, and artificial intelligence.
           b) Discuss how this interdisciplinary approach enhances the potential accuracy of your predictions.
           c) Suggest potential applications of your AI system in other fields or areas of research.

        Ensure your response demonstrates a deep understanding of historical linguistics, language evolution theories, and AI system design. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

        Format your response with clear headings for each section, numbered as above. Include the word count at the end of each section in parentheses. Your total response should be between 1400-1700 words. Include a total word count at the end of your response.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately analyzes historical language evolution patterns in {t['language']}.",
            f"The future predictions for {t['linguistic_aspect']} are well-reasoned and consider the influence of {t['social_factor']}.",
            "The proposed AI system design is innovative yet scientifically plausible.",
            "The response demonstrates a deep understanding of historical linguistics, language evolution theories, and AI system design.",
            "The ethical and societal implications are thoroughly analyzed.",
            "The response shows a high level of interdisciplinary knowledge integration and creative problem-solving.",
            "The response adheres to the specified word limits for each section and includes word counts as instructed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
