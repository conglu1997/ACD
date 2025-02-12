import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "language_family": "Indo-European",
                "phonological_features": ["voicing", "place of articulation", "manner of articulation"],
                "cultural_aspect": "kinship system",
                "number_range": "0 to 20"
            },
            {
                "language_family": "Sino-Tibetan",
                "phonological_features": ["tone", "aspiration", "vowel length"],
                "cultural_aspect": "color symbolism",
                "number_range": "0 to 15"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a number system based on phonological features of the {t['language_family']} language family and use it to encode cultural information about {t['cultural_aspect']}. Your task has the following parts:\n\n1. Number System Design (200-250 words):\n   a) Create a system to represent numbers from {t['number_range']} using the phonological features: {', '.join(t['phonological_features'])}.\n   b) Explain how your system represents at least five numbers within the given range.\n   c) Describe how these phonological features are typically used in the {t['language_family']} language family.\n   d) Explain how your number system reflects or incorporates aspects of the language family's phonology.\n\n2. Cultural Encoding (200-250 words):\n   a) Describe how your number system can be used to encode information about {t['cultural_aspect']}.\n   b) Provide at least three examples of cultural information encoded in your number system.\n   c) Explain the significance of these encoded cultural elements.\n\n3. Mathematical Operations (150-200 words):\n   a) Explain how your system performs addition and multiplication.\n   b) Provide an example of each operation using numbers from your system.\n   c) Discuss how these operations might reflect or relate to cultural concepts.\n\n4. Comparative Analysis (150-200 words):\n   a) Compare your phonological number system to the traditional number system used in the {t['language_family']} language family.\n   b) Discuss one advantage and one limitation of your system for encoding cultural information.\n   c) Explain how your system might influence or be influenced by the cognitive processes of speakers from this language family.\n\n5. Interdisciplinary Implications (100-150 words):\n   Discuss potential applications or implications of your phonological number system in fields such as anthropology, cognitive science, or cryptography.\n\nEnsure your response is creative, linguistically sound, and culturally sensitive. Demonstrate a deep understanding of phonology, number systems, and cultural analysis throughout your answer."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The number system is based on the phonological features of the {t['language_family']} language family.",
            f"The system can represent numbers from {t['number_range']}.",
            f"The cultural encoding relates to {t['cultural_aspect']}.",
            "The response includes examples of addition and multiplication using the designed number system.",
            "The comparative analysis discusses advantages and limitations of the system.",
            "The response demonstrates creativity and interdisciplinary knowledge application.",
            "The answer is well-structured and follows the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
