import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        math_concepts = [
            "complex numbers",
            "topology",
            "differential equations",
            "group theory",
            "non-Euclidean geometry",
            "fractals",
            "chaos theory",
            "quantum mechanics"
        ]
        sensory_modalities = [
            "visual",
            "auditory",
            "tactile",
            "proprioceptive",
            "olfactory"
        ]
        applications = [
            "mathematics education",
            "data visualization",
            "accessibility for visually impaired",
            "AI training and reasoning",
            "artistic expression",
            "scientific communication"
        ]
        return {
            "1": {
                "concept": random.choice(math_concepts),
                "primary_modality": random.choice(sensory_modalities),
                "secondary_modality": random.choice([m for m in sensory_modalities if m != "primary_modality"]),
                "application": random.choice(applications)
            },
            "2": {
                "concept": random.choice(math_concepts),
                "primary_modality": random.choice(sensory_modalities),
                "secondary_modality": random.choice([m for m in sensory_modalities if m != "primary_modality"]),
                "application": random.choice(applications)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that translates the abstract mathematical concept of {t['concept']} into a multi-sensory experience, primarily using the {t['primary_modality']} modality and secondarily the {t['secondary_modality']} modality. Then, analyze its potential application in {t['application']}. Your response should include:

1. Conceptual Analysis (200-250 words):
   a) Explain the key characteristics and principles of {t['concept']}.
   b) Discuss the challenges in representing this concept through sensory experiences.
   c) Analyze how {t['primary_modality']} and {t['secondary_modality']} modalities might be particularly suited (or challenging) for representing aspects of this concept.

2. Translation System Design (250-300 words):
   a) Describe the overall architecture of your math-to-sensory translation system.
   b) Explain the key components and their functions.
   c) Detail how your system would represent {t['concept']} using {t['primary_modality']} and {t['secondary_modality']} experiences.
   d) Provide a specific example of how a particular aspect of {t['concept']} would be translated into these sensory modalities.

3. Cognitive and Perceptual Considerations (200-250 words):
   a) Analyze how your sensory representation might affect understanding and intuition of {t['concept']}.
   b) Discuss potential cognitive advantages or disadvantages of experiencing mathematical concepts in this way.
   c) Consider how individual differences in sensory processing might impact the effectiveness of your system.

4. Application Analysis (200-250 words):
   a) Explore how your system could be applied in the field of {t['application']}.
   b) Provide two specific examples of how it might be used in this context.
   c) Discuss potential benefits and limitations of using your system in this application.

5. Implementation and Technical Challenges (150-200 words):
   a) Identify key technical challenges in implementing your system.
   b) Propose potential solutions or areas for future research to address these challenges.
   c) Discuss any specific technologies or techniques that would be crucial for realizing your design.

6. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical considerations related to translating mathematical concepts into sensory experiences.
   b) Consider how widespread adoption of such systems might impact mathematics education and research.
   c) Explore any potential risks or unintended consequences of this technology.

Ensure your response demonstrates a deep understanding of mathematics, sensory perception, and cognitive science. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, numbered as above. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively designs a system to translate {t['concept']} into {t['primary_modality']} and {t['secondary_modality']} sensory experiences.",
            "The translation system design is well-explained, scientifically plausible, and includes specific examples.",
            "The response demonstrates a deep understanding of the mathematical concept, sensory perception, and cognitive science.",
            f"The application analysis for {t['application']} is thorough and includes realistic examples and considerations.",
            "The response addresses technical challenges, ethical implications, and societal impacts of the proposed system.",
            "The response is creative and innovative while maintaining scientific rigor.",
            "The response follows the specified format, including clear headings and staying within the word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
