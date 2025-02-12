import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            {
                'domain': 'education',
                'start_year': 1900,
                'end_year': 2023,
                'future_year': 2100
            },
            {
                'domain': 'transportation',
                'start_year': 1800,
                'end_year': 2023,
                'future_year': 2150
            },
            {
                'domain': 'healthcare',
                'start_year': 1950,
                'end_year': 2023,
                'future_year': 2075
            },
            {
                'domain': 'communication',
                'start_year': 1850,
                'end_year': 2023,
                'future_year': 2125
            }
        ]
        selected_domains = random.sample(domains, 2)
        return {str(i+1): domain for i, domain in enumerate(selected_domains)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that analyzes historical societal trends and predicts future societal developments in the domain of {t['domain']}. Your system should analyze trends from {t['start_year']} to {t['end_year']} and make predictions for the year {t['future_year']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for temporal societal analysis and prediction.
   b) Explain how your system processes and integrates historical data from various sources.
   c) Detail the predictive modeling techniques used for future projections.
   d) Discuss any novel approaches or algorithms you've incorporated to handle the complexity of societal trends.

2. Historical Analysis (250-300 words):
   a) Explain how your system identifies and analyzes key trends in the given domain from {t['start_year']} to {t['end_year']}.
   b) Describe the methods used to account for the reliability and biases in historical data.
   c) Provide an example of how your system would interpret a specific historical event or trend in the context of broader societal changes.

3. Predictive Modeling (250-300 words):
   a) Detail the approach your system uses to extrapolate future trends based on historical data.
   b) Explain how your model accounts for potential disruptions or paradigm shifts.
   c) Describe how the system quantifies and communicates the uncertainty in its predictions.

4. Interdisciplinary Integration (200-250 words):
   a) Explain how your system incorporates knowledge from multiple disciplines (e.g., sociology, economics, technology) in its analysis and predictions.
   b) Discuss any challenges in reconciling potentially conflicting data or theories from different fields.

5. Case Study: Future Prediction (300-350 words):
   a) Present a detailed prediction for the state of {t['domain']} in the year {t['future_year']}.
   b) Explain the key factors and historical trends that led to this prediction.
   c) Discuss potential alternative scenarios and their probabilities.

6. Ethical Considerations and Limitations (200-250 words):
   a) Identify potential ethical issues related to predicting future societal developments.
   b) Discuss the limitations of your system and the reliability of long-term predictions.
   c) Propose guidelines for the responsible use of AI-generated future predictions in policy-making and planning.

Ensure your response demonstrates a deep understanding of historical analysis, predictive modeling, and the chosen domain. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1500-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of historical trends and future projections in the domain of {t['domain']}.",
            "The AI system design effectively integrates historical analysis, predictive modeling, and interdisciplinary knowledge.",
            f"The case study provides a detailed and plausible prediction for {t['domain']} in the year {t['future_year']}, with justifications based on historical trends.",
            "The response shows creativity and innovation in designing the AI system while maintaining scientific plausibility.",
            "The ethical considerations and limitations are thoroughly addressed.",
            "The response follows the specified format and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
