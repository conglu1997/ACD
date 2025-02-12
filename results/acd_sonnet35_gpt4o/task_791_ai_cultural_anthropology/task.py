import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            "Subterranean cavern system with bioluminescent flora",
            "Floating islands in a gas giant's atmosphere"
        ]
        social_structures = [
            "Matriarchal gerontocracy",
            "Meritocratic techno-shamanism"
        ]
        technological_levels = [
            "Bronze Age equivalent with unique energy source",
            "Post-scarcity society with limited space travel"
        ]
        return {
            "1": {
                "environment": random.choice(environments),
                "social_structure": random.choice(social_structures),
                "tech_level": random.choice(technological_levels)
            },
            "2": {
                "environment": random.choice(environments),
                "social_structure": random.choice(social_structures),
                "tech_level": random.choice(technological_levels)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create and analyze a fictional culture based on the following parameters:

Environment: {t['environment']}
Social Structure: {t['social_structure']}
Technological Level: {t['tech_level']}

Your task has the following parts:

1. Cultural Design (300-350 words):
   a) Describe the key aspects of this culture, including beliefs, values, social norms, and daily life.
   b) Explain how the given parameters have shaped the culture's development.
   c) Create a unique cultural practice or tradition that reflects the interplay of the given parameters.

2. Material Culture (200-250 words):
   a) Describe 3-5 significant artifacts or technologies used by this culture.
   b) Explain how these items reflect the culture's environment, social structure, and technological level.
   c) Discuss how these artifacts might be misinterpreted by an outside observer.

3. Cultural Evolution Prediction (250-300 words):
   a) Predict how this culture might evolve over the next 500 years.
   b) Identify key factors that would drive this evolution.
   c) Describe a potential conflict or challenge the culture might face and how it could adapt.

4. Anthropological Analysis (200-250 words):
   a) Apply two anthropological theories or concepts to analyze this culture.
   b) Compare and contrast this fictional culture with a real-world culture or historical civilization.
   c) Discuss what studying this fictional culture could reveal about human societies in general.

5. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of creating and studying fictional cultures.
   b) Address potential biases or assumptions in your cultural design and analysis.
   c) Propose guidelines for responsible speculative anthropology.

Ensure your response demonstrates a deep understanding of anthropological principles, creative problem-solving, and the ability to synthesize complex cultural concepts. Use appropriate terminology and provide clear explanations for your design choices and analyses.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of anthropological principles and cultural dynamics.",
            "The fictional culture is creative, internally consistent, and reflects the given parameters.",
            "The cultural evolution prediction is plausible and well-reasoned.",
            "The anthropological analysis applies relevant theories and draws insightful comparisons.",
            "The ethical considerations are thoughtful and demonstrate awareness of potential issues in speculative anthropology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
