import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultural_traditions = [
            {
                "culture": "Indian Classical",
                "mathematical_concept": "Fibonacci sequence in tala structures",
                "musical_element": "Rhythmic patterns in Carnatic music"
            },
            {
                "culture": "Western Classical",
                "mathematical_concept": "Golden ratio in sonata form",
                "musical_element": "Harmonic progressions in Baroque music"
            },
            {
                "culture": "West African",
                "mathematical_concept": "Polyrhythmic ratios",
                "musical_element": "Djembe drumming patterns"
            },
            {
                "culture": "Chinese Traditional",
                "mathematical_concept": "Pentatonic scale ratios",
                "musical_element": "Melodic structures in Guqin music"
            }
        ]
        return {
            "1": random.choice(cultural_traditions),
            "2": random.choice(cultural_traditions)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Analyze and create musical structures based on mathematical principles from the {t['culture']} tradition, focusing on the {t['mathematical_concept']} and its application to {t['musical_element']}. Then, compose a short piece combining these elements with a contrasting musical tradition of your choice. Your response should include:\n\n1. Mathematical Analysis (150-200 words):\n   a) Explain the {t['mathematical_concept']} and its relevance to music theory.\n   b) Describe how this concept is applied in {t['musical_element']}.\n   c) Provide a mathematical representation or formula related to this concept.\n\n2. Cultural Context (100-150 words):\n   a) Briefly describe the cultural significance of {t['musical_element']} in {t['culture']} music.\n   b) Explain how the mathematical structure reflects or enhances cultural expression.\n\n3. Musical Structure Creation (200-250 words):\n   a) Design a musical structure (e.g., rhythm pattern, melodic sequence, or harmonic progression) that incorporates the {t['mathematical_concept']}.\n   b) Explain how your structure mathematically aligns with the concept.\n   c) Describe how this structure would be performed or notated in traditional {t['culture']} music.\n\n4. Cross-Cultural Composition (250-300 words):\n   a) Choose a contrasting musical tradition to combine with the {t['culture']} elements you've analyzed.\n   b) Compose a short piece (describe in words, no actual notation required) that blends elements from both traditions.\n   c) Explain how you've incorporated the mathematical concepts and cultural elements from both traditions.\n   d) Discuss any challenges or interesting synergies you encountered in this fusion.\n\n5. Reflection (100-150 words):\n   a) Discuss how this exercise demonstrates the universality of mathematical principles in music across cultures.\n   b) Reflect on the potential benefits and drawbacks of applying mathematical analysis to cultural music traditions.\n\nEnsure your response demonstrates a deep understanding of music theory, mathematical concepts, and cultural sensitivity. Be creative in your musical structure and composition while maintaining mathematical and cultural accuracy."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains the {t['mathematical_concept']} and its application to {t['musical_element']}.",
            f"The cultural context of {t['musical_element']} in {t['culture']} music is appropriately described.",
            "A valid musical structure incorporating the given mathematical concept is created and explained.",
            "The cross-cultural composition successfully blends elements from two distinct musical traditions.",
            "The reflection demonstrates understanding of the universality of mathematical principles in music across cultures.",
            "The response shows creativity, cultural sensitivity, and accurate application of music theory and mathematical concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
