import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        urban_elements = [
            "street signs",
            "shop fronts",
            "billboards",
            "graffiti",
            "public transport signage"
        ]
        linguistic_aspects = [
            "language mixing",
            "script variation",
            "translanguaging",
            "language hierarchies",
            "diachronic changes"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "urban_element": random.choice(urban_elements),
                "linguistic_aspect": random.choice(linguistic_aspects),
                "sample_data": [
                    {"text": "SALE 特価 SOLDES", "location": "shop window", "languages": ["English", "Japanese", "French"]},
                    {"text": "STOP ARRÊT 停", "location": "street corner", "languages": ["English", "French", "Chinese"]},
                    {"text": "Kebab पिज़्ज़ा Sushi", "location": "food court sign", "languages": ["English", "Hindi", "Japanese"]}
                ]
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to analyze and interpret linguistic landscapes in urban environments, focusing on {t['urban_element']} and {t['linguistic_aspect']}. Your response should include the following sections:

1. Theoretical Framework (200-250 words):
   a) Explain the concept of linguistic landscapes and their significance in urban sociolinguistics.
   b) Discuss the relevance of {t['urban_element']} and {t['linguistic_aspect']} in linguistic landscape analysis.
   c) Propose a hypothesis about how AI could provide new insights into these aspects of linguistic landscapes.

2. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for analyzing linguistic landscapes.
   b) Explain how your system integrates computer vision and natural language processing techniques.
   c) Detail how the system accounts for spatial distribution and visual context of linguistic elements.
   d) Discuss how your system handles multilingual text and script variation.

3. Data Collection and Processing (200-250 words):
   a) Outline a method for collecting representative data of {t['urban_element']} in diverse urban environments.
   b) Describe how you would preprocess and annotate the data for machine learning.
   c) Explain how you would ensure your dataset captures the complexity of {t['linguistic_aspect']}.
   d) Discuss potential biases in data collection and how you would address them.

4. Analysis and Interpretation Methodology (200-250 words):
   a) Describe how your AI system would analyze {t['urban_element']} to extract insights about {t['linguistic_aspect']}.
   b) Explain how the system would account for cultural and historical context in its analysis.
   c) Propose a method for visualizing and presenting the AI's findings to researchers and urban planners.
   d) Discuss how you would validate the accuracy and reliability of your system's interpretations.

5. Ethical Considerations and Societal Impact (150-200 words):
   a) Discuss potential ethical issues in using AI to analyze linguistic landscapes.
   b) Explain how your system would handle sensitive or controversial linguistic content.
   c) Explore the potential impact of your AI system on urban planning and language policy.
   d) Propose guidelines for the responsible use of AI in linguistic landscape research.

6. Interdisciplinary Applications and Future Directions (150-200 words):
   a) Suggest two novel applications of your AI system in fields other than sociolinguistics.
   b) Discuss how your approach could be extended to analyze digital linguistic landscapes (e.g., social media, online forums).
   c) Propose a research question that arises from the capabilities of your AI system.

7. Sample Data Analysis (100-150 words):
   Analyze the following sample data using your proposed AI system:
   {t['sample_data']}
   Explain how your system would interpret this data in the context of {t['linguistic_aspect']}.

Ensure your response demonstrates a deep understanding of sociolinguistics, urban studies, computer vision, and natural language processing. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section and subsections where appropriate. Your total response should be between 1250-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a clear explanation of linguistic landscapes and their significance, with specific focus on {t['urban_element']} and {t['linguistic_aspect']}",
            "The AI system architecture should be described in detail, integrating computer vision and natural language processing techniques",
            "The data collection and processing methodology should be clearly outlined, addressing potential biases",
            "The analysis and interpretation methodology should be well-explained, including methods for visualizing and validating results",
            "Ethical considerations and societal impacts of using AI for linguistic landscape analysis should be thoroughly discussed",
            "The response should propose novel interdisciplinary applications and future research directions",
            "The proposed AI system should be creative and innovative while maintaining scientific plausibility",
            "The response should demonstrate a deep understanding of sociolinguistics, urban studies, computer vision, and natural language processing",
            f"The sample data analysis should provide insightful interpretation related to {t['linguistic_aspect']}",
            "The response should be well-structured with clear headings and subheadings as specified in the instructions"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
