import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {
                "name": "Ainu",
                "location": "Japan",
                "language_family": "Language isolate",
                "unique_features": ["Complex verb structure", "Rich oral tradition", "Nature-centric worldview"]
            },
            {
                "name": "Quechua",
                "location": "Andean region of South America",
                "language_family": "Quechuan",
                "unique_features": ["Evidentiality markers", "Agglutinative morphology", "Inca heritage"]
            }
        ]
        return {
            "1": {"culture": random.choice(cultures)},
            "2": {"culture": random.choice(cultures)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        culture = t['culture']
        return f"""Design an AI system to preserve and evolve the {culture['name']} language and culture. Your task is to:

1. Outline the key components of your AI system (150-200 words), including:
   a) Data collection methods
   b) Language modeling approach
   c) Cultural knowledge representation
   d) Interface for community interaction

2. Explain how your system would address these specific challenges (100-150 words each):
   a) Preserving the {culture['unique_features'][0]} of the {culture['name']} language
   b) Evolving the language to include modern concepts while maintaining its {culture['unique_features'][2]}

3. Provide an example of how your AI system would generate a new word or phrase in the {culture['name']} language for a modern concept (e.g., 'social media', 'climate change', or 'artificial intelligence'). Explain your reasoning. (50-100 words)

4. Analyze the potential positive and negative impacts of your AI system on the {culture['name']} community and their culture. Consider ethical implications, potential biases, and unintended consequences. (200-250 words)

5. Propose a method to evaluate the effectiveness and cultural sensitivity of your AI system. (100-150 words)

Ensure your response demonstrates a deep understanding of linguistic principles, cultural preservation challenges, and AI ethics. Be creative in your solutions while remaining sensitive to the unique aspects of the {culture['name']} culture."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all five required sections comprehensively.",
            f"The AI system design is tailored to the specific needs of the {t['culture']['name']} culture and language.",
            "The response demonstrates a nuanced understanding of the challenges in language preservation and evolution.",
            "The example of generating a new word or phrase is creative and culturally appropriate.",
            "The analysis of potential impacts is balanced, considering both positive and negative consequences.",
            "The proposed evaluation method is practical and considers cultural sensitivity.",
            "The overall response shows interdisciplinary thinking, combining linguistics, anthropology, and AI."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
