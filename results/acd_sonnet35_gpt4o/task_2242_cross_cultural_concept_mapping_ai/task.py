import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = ["Ancient Mayan", "Modern Japanese", "Inuit", "Renaissance Italian", "Zulu"]
        domains = ["Time", "Kinship", "Morality", "Nature", "Causality"]
        concepts = ["Balance", "Cycles", "Harmony", "Progress", "Interconnectedness"]
        
        tasks = {
            "1": {
                "culture": random.choice(cultures),
                "domain": random.choice(domains),
                "concept": random.choice(concepts)
            },
            "2": {
                "culture": random.choice(cultures),
                "domain": random.choice(domains),
                "concept": random.choice(concepts)
            }
        }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting abstract conceptual schemas across different cultures and domains, then apply it to the following scenario:

Culture: {t['culture']}
Domain: {t['domain']}
Concept to Map: {t['concept']}

Your task has the following parts:

1. Conceptual Schema Generation Framework (200-250 words):
   Explain the cognitive processes involved in creating abstract conceptual schemas. Describe how your AI system would implement these processes, considering cultural variations.

2. AI System Architecture (200-250 words):
   Provide a high-level overview of your AI system's architecture and its unique features for cross-cultural concept mapping.

3. Application to the Given Scenario (250-300 words):
   Apply your AI system to generate an abstract conceptual schema for the given concept in the specified culture and domain. Provide a detailed explanation of the schema and the system's process.

4. Schema Interpretation (150-200 words):
   Describe how your AI system would interpret and explain conceptual schemas from other cultures, addressing potential challenges and biases.

5. Cross-Cultural Comparison (150-200 words):
   Demonstrate how your AI system would compare the generated schema with conceptualizations of the same concept in at least two other cultures.

6. Evaluation and Refinement (100-150 words):
   Propose a method for evaluating the accuracy and cultural sensitivity of the generated schemas, and describe how your AI system would improve its process based on feedback.

7. Ethical and Societal Implications (100-150 words):
   Discuss potential ethical implications and societal impacts of this technology, particularly in the context of cross-cultural understanding and AI development.

Ensure your response demonstrates a deep understanding of cognitive linguistics, cultural anthropology, and AI system design. Be creative and innovative while maintaining scientific rigor and cultural sensitivity. Your total response should be between 1150-1500 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive processes involved in conceptual schema creation.",
            "The AI system architecture is well-designed and suitable for cross-cultural concept mapping.",
            "The application to the given scenario is thorough and culturally sensitive.",
            "The schema interpretation process is well-explained and addresses potential challenges.",
            "The cross-cultural comparison is insightful and demonstrates the system's capability to understand diverse perspectives.",
            "The evaluation method is appropriate and the refinement process is well-thought-out.",
            "Ethical and societal implications are thoroughly considered.",
            "The response shows creativity and innovation while maintaining scientific rigor.",
            "The writing is clear, well-structured, and adheres to the specified word counts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
