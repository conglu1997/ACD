import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        alien_civilizations = [
            {
                "name": "Luminarians",
                "biology": "Bioluminescent, telepathic floating orbs",
                "environment": "Gas giant with dense atmosphere",
                "culture": "Collective consciousness, no concept of individuality"
            },
            {
                "name": "Chrono-Shifters",
                "biology": "Silicon-based lifeforms that experience time non-linearly",
                "environment": "Tidally locked planet with extreme temperature variations",
                "culture": "Focused on preserving and manipulating temporal energy"
            }
        ]
        return {
            "1": random.choice(alien_civilizations),
            "2": random.choice(alien_civilizations)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language model for the {t['name']} civilization. Consider their unique characteristics:

Biology: {t['biology']}
Environment: {t['environment']}
Culture: {t['culture']}

Your task is to:

1. Describe the key features of their language, considering their biology and environment (3-4 sentences).
2. Explain how their cultural characteristics would influence the structure and use of their language (2-3 sentences).
3. Propose a novel approach for designing an AI language model that could effectively process and generate this alien language (4-5 sentences). Consider:
   a) Input and output modalities
   b) Data structures and algorithms
   c) Potential challenges and solutions
4. Discuss how this alien AI language model might differ from human language models in terms of architecture and training process (3-4 sentences).
5. Suggest a potential application or use case for this alien AI language model within their civilization (2-3 sentences).

Ensure your response demonstrates a clear understanding of linguistics, cultural anthropology, and artificial intelligence principles, while creatively applying these concepts to the alien civilization."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should demonstrate a clear understanding of linguistic principles and how they apply to the alien civilization's characteristics.",
            "The explanation of cultural influences on language should be logical and well-reasoned.",
            "The proposed AI language model approach should be innovative and tailored to the alien civilization's unique features.",
            "The comparison between alien and human AI language models should show insight into AI principles and potential variations.",
            "The suggested application should be relevant and creative, considering the alien civilization's needs and capabilities.",
            "The overall response should be coherent, well-structured, and demonstrate interdisciplinary thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
