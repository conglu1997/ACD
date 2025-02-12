import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultural_metaphors = [
            {
                "culture": "Japanese",
                "concept": "Life",
                "metaphor": "Life is a journey"
            },
            {
                "culture": "Native American (Lakota)",
                "concept": "Time",
                "metaphor": "Time is a circle"
            },
            {
                "culture": "Ancient Greek",
                "concept": "Knowledge",
                "metaphor": "Knowledge is light"
            },
            {
                "culture": "Chinese",
                "concept": "Balance",
                "metaphor": "Balance is Yin and Yang"
            }
        ]
        return {
            "1": random.choice(cultural_metaphors),
            "2": random.choice(cultural_metaphors)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Analyze the culturally-specific metaphor '{t['metaphor']}' from {t['culture']} culture, which represents the concept of {t['concept']}. Then, create a new metaphor for the same concept that would be meaningful in a different culture of your choice. Your response should include:\n\n1. Analysis of the given metaphor (200-250 words):\n   a) Explain the cultural significance of the metaphor.\n   b) Discuss how it reflects the worldview or values of the {t['culture']} culture.\n   c) Analyze the relationship between the concrete imagery and the abstract concept.\n\n2. Creation of a new metaphor (200-250 words):\n   a) Choose a different culture and briefly explain your choice.\n   b) Create a new metaphor for {t['concept']} that would resonate in this culture.\n   c) Explain the cultural significance of your new metaphor.\n   d) Discuss how it reflects the worldview or values of the chosen culture.\n   Note: Try to consider less obvious or stereotypical aspects of the culture when creating your metaphor.\n\n3. Comparative analysis (150-200 words):\n   a) Compare and contrast the original metaphor with your created one.\n   b) Discuss how the different cultural contexts influence the representation of {t['concept']}.\n   c) Reflect on what these differences reveal about cultural perspectives on {t['concept']}.\n\n4. Universal themes (100-150 words):\n   a) Identify any universal themes or commonalities in how {t['concept']} is conceptualized across these cultures.\n   b) Discuss the implications of these commonalities for cross-cultural understanding.\n\n5. Potential applications (100-150 words):\n   a) Suggest how understanding culturally-specific metaphors could be valuable in fields such as international relations, marketing, or education.\n   b) Propose a specific scenario where this kind of cross-cultural metaphor analysis could be applied.\n\nEnsure your response demonstrates a deep understanding of cultural contexts, linguistic creativity, and analytical reasoning. Use appropriate terminology and provide clear explanations. Your total response should be between 750-1000 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately analyzes the given {t['culture']} metaphor for {t['concept']}.",
            "A new, culturally-appropriate metaphor is created for a different culture, showing originality and avoiding stereotypes.",
            "The comparative analysis demonstrates insight into how cultural contexts influence metaphorical representations.",
            "Universal themes are identified and discussed thoughtfully.",
            "The potential applications suggested are practical and well-reasoned.",
            "The response shows creativity, cultural sensitivity, and a deep understanding of metaphorical thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
