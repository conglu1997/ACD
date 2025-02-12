import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            "Inuit",
            "Maori",
            "Bedouin",
            "Yanomami",
            "Tibetan",
            "Maasai"
        ]
        cognitive_processes = [
            "spatial reasoning",
            "time perception",
            "color categorization",
            "kinship systems",
            "numerical cognition",
            "emotional expression"
        ]
        linguistic_features = [
            "evidentiality markers",
            "honorifics",
            "grammatical gender",
            "tense systems",
            "counting systems",
            "ideophones"
        ]
        return {
            "1": {
                "source_culture": random.choice(cultures),
                "target_culture": random.choice(cultures),
                "cognitive_process": random.choice(cognitive_processes),
                "linguistic_feature": random.choice(linguistic_features)
            },
            "2": {
                "source_culture": random.choice(cultures),
                "target_culture": random.choice(cultures),
                "cognitive_process": random.choice(cognitive_processes),
                "linguistic_feature": random.choice(linguistic_features)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that translates not just language, but cultural context and neurolinguistic patterns between the {t['source_culture']} and {t['target_culture']} cultures, with a focus on the cognitive process of {t['cognitive_process']} and the linguistic feature of {t['linguistic_feature']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI neurolinguistic cultural translation system.
   b) Explain how your system integrates knowledge from neuroscience, linguistics, and cultural anthropology.
   c) Detail how the system analyzes and translates the specified cognitive process and linguistic feature.
   d) Include a high-level diagram of your system architecture (describe it in words).

2. Data Collection and Processing (250-300 words):
   a) Explain your approach to collecting and processing neurolinguistic and cultural data for both cultures.
   b) Discuss how you ensure data quality and handle potential biases or gaps in the data.
   c) Describe any novel techniques used for integrating diverse data types (e.g., neuroimaging, linguistic corpora, ethnographic data).

3. Translation and Analysis Process (250-300 words):
   a) Detail how your AI system translates the specified cognitive process between the two cultures.
   b) Explain how the system handles the translation of the given linguistic feature.
   c) Discuss how your system accounts for cultural context in its translations and analyses.

4. Cognitive Impact Assessment (200-250 words):
   a) Describe how your system evaluates the impact of translation on cognitive processes.
   b) Explain any predictive models used to anticipate cognitive shifts resulting from cultural-linguistic translation.
   c) Discuss how the system might identify and analyze cognitive universals vs. culture-specific patterns.

5. Ethical Considerations and Safeguards (200-250 words):
   a) Identify potential ethical issues in using AI for neurolinguistic and cultural translation.
   b) Propose guidelines for responsible development and deployment of your system.
   c) Discuss how your system would respect and preserve cultural diversity and indigenous knowledge.

6. Applications and Implications (150-200 words):
   a) Suggest potential applications of your system in fields such as cross-cultural communication, education, or conflict resolution.
   b) Discuss the implications of your system for our understanding of the relationship between language, culture, and cognition.
   c) Explore how this technology could impact global intercultural dynamics.

Ensure your response demonstrates a deep understanding of neurolinguistics, cultural anthropology, and artificial intelligence. Be creative in your approach while maintaining scientific accuracy and cultural sensitivity. Use appropriate terminology from all relevant fields and provide clear explanations for technical terms where necessary.

Format your response with clear headings for each section, numbered as above. Use subheadings (a, b, c) where indicated. Your total response should be between 1350-1650 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a comprehensive design of an AI system for neurolinguistic cultural translation between {t['source_culture']} and {t['target_culture']} cultures, focusing on {t['cognitive_process']} and {t['linguistic_feature']}.",
            "The system architecture is well-described and effectively integrates knowledge from neuroscience, linguistics, and cultural anthropology.",
            "The data collection and processing approach is well-explained and addresses potential biases and data integration challenges.",
            "The translation and analysis process for the specified cognitive process and linguistic feature is clearly detailed and considers cultural context.",
            "The cognitive impact assessment methodology is thoroughly described, including predictive models and analysis of cognitive patterns.",
            "Ethical considerations are thoughtfully addressed with proposed guidelines for responsible use and preservation of cultural diversity.",
            "The response suggests relevant applications and discusses implications for understanding language, culture, and cognition.",
            "The response demonstrates creativity, interdisciplinary knowledge integration, and cultural sensitivity within the given word limit (1350-1650 words).",
            "Technical terms are appropriately used and explained for clarity."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
