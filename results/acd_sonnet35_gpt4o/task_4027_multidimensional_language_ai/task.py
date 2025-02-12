import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        abstract_concepts = [
            "Infinity",
            "Consciousness",
            "Causality",
            "Free will",
            "Existence"
        ]
        dimensions = [
            "Temporal",
            "Spatial",
            "Conceptual",
            "Emotional",
            "Quantum"
        ]
        return {
            "1": {
                "concept": random.choice(abstract_concepts),
                "dimension1": random.choice(dimensions),
                "dimension2": random.choice(dimensions)
            },
            "2": {
                "concept": random.choice(abstract_concepts),
                "dimension1": random.choice(dimensions),
                "dimension2": random.choice(dimensions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting a hypothetical 'multidimensional language' that transcends linear time and three-dimensional space. Then, apply your system to express and analyze the abstract concept of {t['concept']}, focusing on the {t['dimension1']} and {t['dimension2']} dimensions. Your response should include the following sections:

1. Multidimensional Language Framework (300-350 words):
   a) Define the key characteristics of your multidimensional language.
   b) Explain how it transcends linear time and three-dimensional space.
   c) Describe how it incorporates the {t['dimension1']} and {t['dimension2']} dimensions.
   d) Discuss the cognitive implications of perceiving and processing this language.

2. AI System Architecture (250-300 words):
   a) Outline the key components of your AI system for generating and interpreting the multidimensional language.
   b) Explain how your system processes and represents information beyond traditional spatiotemporal constraints.
   c) Describe any novel algorithms or techniques used in your system.
   d) Discuss how your AI system interfaces with human users or other AI systems.

3. Expressing the Abstract Concept (250-300 words):
   a) Use your multidimensional language to express the concept of {t['concept']}.
   b) Provide a detailed 'translation' or explanation of how this concept is conveyed.
   c) Analyze how the {t['dimension1']} and {t['dimension2']} dimensions contribute to expressing this concept.
   d) Compare this expression to how the concept might be conveyed in traditional human languages.

4. Analysis and Interpretation (200-250 words):
   a) Describe how your AI system would analyze and interpret the multidimensional expression of {t['concept']}.
   b) Discuss any unique insights or perspectives gained through this multidimensional analysis.
   c) Explain how this approach might enhance our understanding of {t['concept']}.

5. Cognitive and Philosophical Implications (200-250 words):
   a) Discuss how engaging with a multidimensional language might impact human or AI cognition.
   b) Explore the philosophical implications of a language that transcends traditional spatiotemporal constraints.
   c) Consider potential applications or consequences for fields such as cognitive science, AI development, or metaphysics.

6. Challenges and Future Directions (150-200 words):
   a) Identify major challenges in developing and implementing this multidimensional language system.
   b) Propose potential solutions or research directions to address these challenges.
   c) Suggest two extensions or modifications to your system for future exploration.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative and speculative in your approach while maintaining logical consistency and scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the abstract concept of {t['concept']}.",
            f"The multidimensional language framework should incorporate the {t['dimension1']} and {t['dimension2']} dimensions.",
            "The AI system architecture should be clearly explained and demonstrate novel approaches to processing multidimensional information.",
            "The expression and analysis of the abstract concept should demonstrate a clear advantage over traditional language approaches.",
            "The response should include all six required sections with appropriate content and depth.",
            "The explanation should be creative and innovative while maintaining logical consistency and scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
