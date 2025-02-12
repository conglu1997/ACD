import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            "kinship",
            "color perception",
            "time",
            "spatial relations",
            "emotions",
            "ethics"
        ]
        cultures = [
            "Western",
            "East Asian",
            "African",
            "Middle Eastern",
            "South American",
            "Oceanic"
        ]
        time_periods = [
            "Ancient (3000 BCE - 500 CE)",
            "Medieval (500 CE - 1500 CE)",
            "Early Modern (1500 CE - 1800 CE)",
            "Modern (1800 CE - 2000 CE)",
            "Contemporary (2000 CE - present)"
        ]
        return {
            "1": {
                "domain": random.choice(domains),
                "culture1": random.choice(cultures),
                "culture2": random.choice([c for c in cultures if c != "culture1"]),
                "time_period": random.choice(time_periods)
            },
            "2": {
                "domain": random.choice(domains),
                "culture1": random.choice(cultures),
                "culture2": random.choice([c for c in cultures if c != "culture1"]),
                "time_period": random.choice(time_periods)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models the evolution of conceptual structures across cultures and time, then use it to analyze and predict conceptual changes in the domain of {t['domain']}. Your system should focus on comparing {t['culture1']} and {t['culture2']} cultures during the {t['time_period']}. Your response should include:

1. Conceptual Evolution Framework (250-300 words):
   a) Describe the theoretical foundations of your AI system, incorporating relevant theories from cognitive linguistics, anthropology, and historical linguistics.
   b) Explain how your system represents and processes conceptual structures and their changes over time.
   c) Discuss how your framework accounts for cultural differences and interactions in conceptual evolution.

2. AI System Architecture (250-300 words):
   a) Outline the main components of your AI system and their functions.
   b) Explain how your system integrates historical, linguistic, and cultural data to model conceptual evolution.
   c) Describe any novel algorithms or techniques your system uses for analyzing and predicting conceptual changes.
   d) Discuss how your system handles uncertainty and incomplete historical data.

3. Analysis of {t['domain']} (300-350 words):
   a) Apply your AI system to analyze the evolution of concepts related to {t['domain']} in {t['culture1']} and {t['culture2']} cultures during the {t['time_period']}.
   b) Identify key differences and similarities in conceptual structures between the two cultures.
   c) Explain how historical events or cultural interactions might have influenced these conceptual structures.
   d) Provide specific examples of conceptual changes predicted by your system, with explanations.

4. Predictive Modeling (200-250 words):
   a) Use your AI system to predict potential future changes in conceptual structures related to {t['domain']} in both cultures.
   b) Explain the reasoning behind these predictions, based on historical trends and current cultural factors.
   c) Discuss the limitations and uncertainties in these predictions.

5. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the accuracy and reliability of your AI system's analyses and predictions.
   b) Describe how you would validate your system's outputs against historical and anthropological data.
   c) Discuss potential challenges in evaluating such a system and how you'd address them.

6. Implications and Applications (150-200 words):
   a) Discuss the potential implications of your system for our understanding of cultural cognition and conceptual evolution.
   b) Propose two novel applications of your system in fields such as cross-cultural communication, education, or AI development.
   c) Explore how this approach might enhance our understanding of human cognition and cultural dynamics.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, anthropology, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively designs an AI system to model conceptual evolution in the domain of {t['domain']}, comparing {t['culture1']} and {t['culture2']} cultures during the {t['time_period']}.",
            "The conceptual evolution framework and AI system architecture are well-explained, scientifically plausible, and demonstrate interdisciplinary integration.",
            "The analysis of the given domain provides insightful comparisons between the two cultures and offers specific examples of conceptual changes.",
            "The predictive modeling section offers plausible future changes and acknowledges limitations and uncertainties.",
            "The proposed evaluation methods and applications are innovative and demonstrate a deep understanding of the implications of the system.",
            "The response is creative and demonstrates a sophisticated understanding of cognitive science, linguistics, anthropology, and artificial intelligence.",
            "The response follows the specified format and adheres to the word limit guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
