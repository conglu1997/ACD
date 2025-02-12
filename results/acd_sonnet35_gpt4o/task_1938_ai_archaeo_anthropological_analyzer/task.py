import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        civilizations = [
            "Ancient Maya",
            "Indus Valley",
            "Ancient Egypt",
            "Mesopotamia",
            "Ancient Greece",
            "Roman Empire"
        ]
        analysis_types = [
            "artifact distribution",
            "settlement patterns",
            "trade networks",
            "social hierarchies",
            "technological evolution",
            "cultural practices"
        ]
        return {
            "1": {
                "civilization": random.choice(civilizations),
                "analysis_type": random.choice(analysis_types)
            },
            "2": {
                "civilization": random.choice(civilizations),
                "analysis_type": random.choice(analysis_types)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to analyze archaeological and anthropological data for the {t['civilization']} civilization, focusing on {t['analysis_type']}. Your response should include the following sections:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for archaeological and anthropological analysis.
   b) Explain how your system integrates multiple data sources (e.g., artifacts, geological data, historical texts).
   c) Detail how the system processes and analyzes data to reconstruct aspects of the {t['civilization']} civilization.
   d) Discuss any novel AI techniques or algorithms used in your system.

2. Data Analysis and Pattern Recognition (200-250 words):
   a) Explain your approach to analyzing {t['analysis_type']} in the context of {t['civilization']}.
   b) Describe how your AI system identifies patterns and makes inferences from incomplete or fragmented data.
   c) Discuss how the system accounts for potential biases or gaps in the archaeological record.

3. Predictive Modeling (200-250 words):
   a) Detail how your AI system generates predictions about undiscovered sites, artifacts, or cultural practices related to {t['analysis_type']} in {t['civilization']}.
   b) Explain any machine learning models or algorithms used for predictive analysis.
   c) Discuss how your system validates its predictions and handles uncertainty.

4. Interdisciplinary Integration (150-200 words):
   a) Describe how your AI system integrates knowledge from archaeology, anthropology, history, and other relevant fields.
   b) Explain how this interdisciplinary approach enhances the system's analytical capabilities.
   c) Discuss any challenges in reconciling different disciplinary perspectives or methodologies.

5. Ethical Considerations and Societal Impact (150-200 words):
   a) Identify potential ethical issues in using AI for archaeological and anthropological analysis.
   b) Discuss how your system addresses concerns about cultural sensitivity and indigenous rights.
   c) Explore the potential impact of your AI system on our understanding of human history and cultural heritage.

6. Limitations and Future Directions (100-150 words):
   a) Acknowledge the limitations of your AI system in analyzing {t['civilization']} and {t['analysis_type']}.
   b) Propose future enhancements or research directions to overcome these limitations.
   c) Suggest how your system could be adapted to study other civilizations or analysis types.

Ensure your response demonstrates a deep understanding of AI, archaeology, and anthropology. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary. Include concrete examples or case studies where applicable to illustrate your points.

Format your response with clear headings for each section, numbered as above. Use subheadings (a, b, c) where indicated. Your total response should be between 1050-1400 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of AI applications in analyzing {t['analysis_type']} for the {t['civilization']} civilization.",
            "The AI system design should be innovative yet scientifically plausible.",
            "The response should show a deep understanding of archaeological and anthropological methodologies.",
            "The predictive modeling approach should be well-explained and justified.",
            "The ethical considerations should be comprehensive and thoughtful.",
            "The response should demonstrate strong interdisciplinary integration.",
            "The limitations and future directions should be realistic and insightful.",
            "The overall response should demonstrate creative problem-solving and analytical reasoning.",
            "The response should include concrete examples or case studies where applicable.",
            "The submission should adhere to the specified format and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
