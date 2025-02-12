import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        music_theory_concepts = [
            {
                "concept": "Counterpoint",
                "description": "The relationship between two or more musical lines that are harmonically interdependent yet independent in rhythm and contour."
            },
            {
                "concept": "Modulation",
                "description": "The process of changing from one key to another within a piece of music."
            }
        ]
        return {
            "1": random.choice(music_theory_concepts),
            "2": random.choice(music_theory_concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"You are an AI music theory composer. Your task is to design a musical composition that demonstrates the concept of {t['concept']}. Follow these steps:\n\n1. Composition Design (200-250 words):\n   a) Describe a short musical composition (about 16-32 measures) that showcases {t['concept']}.\n   b) Explain how your composition incorporates the principle of {t['concept']}.\n   c) Detail any specific techniques or structures you've used to highlight this concept.\n\n2. Music Theory Analysis (150-200 words):\n   a) Provide a theoretical analysis of your composition, focusing on how it exemplifies {t['concept']}.\n   b) Explain any challenges you encountered in applying this concept and how you resolved them.\n\n3. Creative Choices (100-150 words):\n   a) Discuss the creative decisions you made in your composition.\n   b) Explain how these choices enhance the demonstration of {t['concept']}.\n\n4. Comparison to Human Composition (100-150 words):\n   a) Compare your AI-generated composition to how a human composer might approach the same task.\n   b) Discuss any unique advantages or limitations of your AI approach.\n\nEnsure your response demonstrates a deep understanding of music theory, particularly {t['concept']}. Use appropriate musical terminology and provide clear explanations for your compositional choices. Be creative in your approach while maintaining musical coherence and theoretical accuracy.\n\nFormat your response with clear headings for each section. Your total response should be between 550-750 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['concept']} in music theory.",
            "The composition design is creative, coherent, and effectively showcases the given concept.",
            "The music theory analysis is accurate and insightful.",
            "The explanation of creative choices is clear and well-reasoned.",
            "The comparison to human composition is thoughtful and demonstrates understanding of AI's unique capabilities and limitations.",
            "The response uses appropriate musical terminology throughout.",
            "The response follows the requested format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0