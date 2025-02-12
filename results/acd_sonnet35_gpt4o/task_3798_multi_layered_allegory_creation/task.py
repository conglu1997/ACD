import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            ("Politics", "Ecology"),
            ("Technology", "Mythology"),
            ("Economics", "Biology"),
            ("Psychology", "Physics")
        ]
        themes = [
            "Power dynamics",
            "Transformation and change",
            "Balance and harmony",
            "Progress and regression"
        ]
        return {
            "1": {
                "domains": random.choice(domains),
                "theme": random.choice(themes)
            },
            "2": {
                "domains": random.choice(domains),
                "theme": random.choice(themes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a complex allegory that incorporates elements from {t['domains'][0]} and {t['domains'][1]}, exploring the theme of {t['theme']}. Your response should include:

1. Allegory Creation (400-500 words):
   a) Write a short allegorical story that integrates concepts from both specified domains.
   b) Ensure your allegory has at least three distinct layers of meaning.
   c) Incorporate the given theme as a central element of your allegory.

2. Analysis of Layers (300-350 words):
   a) Identify and explain the three (or more) layers of meaning in your allegory.
   b) Discuss how each layer relates to the specified domains and theme.
   c) Explain any symbolism or metaphors used in your allegory.

3. Interdisciplinary Connections (200-250 words):
   a) Analyze how your allegory bridges concepts from the two specified domains.
   b) Discuss any novel insights or perspectives that emerge from this interdisciplinary approach.

4. Thematic Exploration (150-200 words):
   a) Explain how your allegory explores the given theme.
   b) Discuss any nuances or complexities of the theme revealed through your allegorical approach.

5. Interpretative Framework (200-250 words):
   a) Propose a method for analyzing and interpreting multi-layered allegories.
   b) Explain how this framework could be applied to other complex narratives or real-world scenarios.

Ensure your response demonstrates deep understanding of the specified domains, creative storytelling, and analytical reasoning. Use appropriate terminology and provide clear explanations for complex concepts. Your total response should be between 1250-1550 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The allegory effectively incorporates elements from both {t['domains'][0]} and {t['domains'][1]}.",
            f"The allegory explores the theme of {t['theme']} in a nuanced and insightful way.",
            "The response identifies and explains at least three distinct layers of meaning in the allegory.",
            "The analysis demonstrates a deep understanding of the interdisciplinary connections between the specified domains.",
            "The proposed interpretative framework is well-reasoned and applicable to other complex narratives."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
