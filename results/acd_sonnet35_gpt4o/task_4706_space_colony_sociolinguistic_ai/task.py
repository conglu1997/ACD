import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "colony_name": "Novaterra",
                "planet_type": "Earth-like",
                "isolation_level": "Moderate",
                "technological_advancement": "Advanced",
                "timeframe": "200 years"
            },
            {
                "colony_name": "Aquarius",
                "planet_type": "Ocean world",
                "isolation_level": "High",
                "technological_advancement": "Moderate",
                "timeframe": "150 years"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to analyze and predict the evolution of language and culture for the space colony {t['colony_name']} on a {t['planet_type']} over a period of {t['timeframe']}. The colony has a {t['isolation_level']} level of isolation from Earth and {t['technological_advancement']} technological advancement. Your response should include the following sections:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for analyzing and predicting sociolinguistic evolution.
   b) Explain how your system integrates data from various sources (e.g., linguistic corpora, cultural artifacts, environmental factors).
   c) Discuss any novel features or innovations in your AI design specific to the space colonization context.

2. Data Collection and Analysis (200-250 words):
   a) Outline the types of data your AI system would collect and analyze.
   b) Explain how your system would handle the challenges of data collection in a space colony setting.
   c) Describe any unique analytical approaches your system employs to process this data.

3. Linguistic Evolution Modeling (250-300 words):
   a) Explain how your AI system models the evolution of language in the space colony.
   b) Discuss factors such as isolation, environmental influences, and technological advancements in your model.
   c) Provide a hypothetical example of a linguistic change your system might predict, with reasoning.

4. Cultural Evolution Prediction (250-300 words):
   a) Describe how your AI system predicts cultural evolution in the space colony.
   b) Analyze the interplay between language change and cultural shifts in your model.
   c) Present a speculative scenario of a significant cultural development predicted by your system.

5. Ethical Considerations and Challenges (150-200 words):
   a) Discuss potential ethical issues in using AI to predict cultural and linguistic evolution.
   b) Address challenges related to bias, data privacy, and the impact of predictions on the colony's development.

6. Interplanetary Comparative Analysis (200-250 words):
   a) Explain how your system would compare sociolinguistic evolution across different space colonies.
   b) Discuss the potential for your AI to identify universal patterns in language and cultural evolution.

7. Future Developments and Applications (150-200 words):
   a) Propose potential improvements or extensions to your AI system.
   b) Suggest how insights from this system could be applied to other fields or back to Earth-based sociolinguistics.

Ensure your response demonstrates a deep understanding of linguistics, anthropology, artificial intelligence, and space science. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative and speculative in your approach while maintaining scientific plausibility. Strive to balance creativity with realistic scenarios based on current scientific understanding.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections comprehensively",
            "The AI system design demonstrates integration of linguistics, anthropology, space science, and artificial intelligence",
            "The solution is innovative and speculative while maintaining scientific plausibility",
            "The response shows a deep understanding of linguistic and cultural evolution in the context of space colonization",
            "The AI system effectively incorporates factors such as isolation, environmental influences, and technological advancements",
            "The response adequately addresses ethical considerations and challenges",
            "The proposed interplanetary comparative analysis and future applications are well-thought-out and insightful",
            "The response balances creativity with realistic scenarios based on current scientific understanding"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
