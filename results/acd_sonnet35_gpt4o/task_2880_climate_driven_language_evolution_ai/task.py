import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            {
                "name": "Inuktitut",
                "region": "Arctic",
                "climate_threat": "Melting ice and permafrost"
            },
            {
                "name": "Swahili",
                "region": "East Africa",
                "climate_threat": "Coastal flooding and drought"
            },
            {
                "name": "Vietnamese",
                "region": "Southeast Asia",
                "climate_threat": "Sea level rise and saltwater intrusion"
            },
            {
                "name": "Quechua",
                "region": "Andean highlands",
                "climate_threat": "Glacial retreat and water scarcity"
            }
        ]
        return {
            "1": random.choice(languages),
            "2": random.choice(languages)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models and predicts the evolution of {t['name']} in response to climate change, particularly the threat of {t['climate_threat']} in the {t['region']} region. Your system should integrate linguistic, environmental, and societal factors to forecast language changes over the next 50 years. Your response should include the following components:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for modeling language evolution.
   b) Explain how these components interact to process linguistic, climate, and societal data.
   c) Discuss how your system incorporates machine learning techniques for prediction.
   d) Include a high-level diagram or pseudocode to illustrate your system's architecture.

2. Data Integration and Preprocessing (200-250 words):
   a) Explain what types of data your system would use (linguistic, climate, demographic, etc.).
   b) Describe how you would preprocess and integrate these diverse data sources.
   c) Discuss any challenges in data collection or integration specific to {t['name']} and the {t['region']} region.

3. Language Evolution Modeling (250-300 words):
   a) Detail how your system models the current state of {t['name']}.
   b) Explain the mechanisms your system uses to predict language changes.
   c) Describe how your model accounts for the impact of {t['climate_threat']} on language evolution.
   d) Provide an example of a potential language change your system might predict, with reasoning.

4. Sociolinguistic Factors (200-250 words):
   a) Explain how your system incorporates social and cultural factors in its predictions.
   b) Discuss how climate-induced migration or lifestyle changes might affect language evolution.
   c) Describe how your model balances linguistic conservatism with innovation driven by environmental pressures.

5. Model Validation and Uncertainty (150-200 words):
   a) Propose methods for validating your system's predictions.
   b) Discuss how your system quantifies and communicates uncertainty in its forecasts.
   c) Explain how you would update and refine the model as new data becomes available.

6. Ethical Considerations and Applications (200-250 words):
   a) Discuss potential ethical issues in predicting language evolution and how you'd address them.
   b) Explore possible applications of your system in language preservation, education, or climate adaptation planning.
   c) Consider the implications of your system for linguistic diversity and cultural heritage.

Ensure your response demonstrates a deep understanding of linguistics, climate science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and use subheadings where appropriate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed and plausible system architecture for modeling language evolution in response to climate change.",
            f"The data integration and preprocessing section adequately addresses the challenges specific to {t['name']} and the {t['region']} region.",
            f"The language evolution modeling component convincingly incorporates the impact of {t['climate_threat']} on language change.",
            "The sociolinguistic factors section demonstrates a nuanced understanding of how climate change might affect social dynamics and language use.",
            "The model validation and uncertainty quantification methods are well-reasoned and appropriate for the task.",
            "The ethical considerations and applications discussion is thoughtful and comprehensive.",
            "The overall response displays creativity, scientific plausibility, and a strong interdisciplinary approach to the problem."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
