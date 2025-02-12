import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mathematical_concepts = [
            {
                "concept": "Fibonacci sequence",
                "description": "A sequence where each number is the sum of the two preceding ones",
                "example": "0, 1, 1, 2, 3, 5, 8, 13, 21, ..."
            },
            {
                "concept": "Golden ratio",
                "description": "A special number approximately equal to 1.618, often found in nature and art",
                "example": "The ratio of a rectangle's long side to its short side is 1.618"
            }
        ]
        return {
            "1": random.choice(mathematical_concepts),
            "2": random.choice(mathematical_concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and create a musical composition based on the mathematical concept of {t['concept']} ({t['description']}). Example: {t['example']}

Your task consists of the following parts:

1. Concept Analysis (200-250 words):
   Explain how the mathematical concept of {t['concept']} can be applied to music composition. Discuss its potential impact on rhythm, melody, harmony, or overall structure.

2. Existing Composition Analysis (250-300 words):
   Identify and analyze an existing musical piece that intentionally or unintentionally incorporates the {t['concept']}. Provide:
   a) The name and composer of the piece
   b) A brief description of the composition
   c) An explanation of how the {t['concept']} is reflected in the music
   d) The impact of this mathematical structure on the listener's experience

3. Original Composition Outline (300-350 words):
   Design an original musical composition based on the {t['concept']}. Provide:
   a) A high-level description of the composition's structure
   b) An explanation of how you've incorporated the {t['concept']} into various musical elements (e.g., rhythm, melody, harmony, form)
   c) A detailed text description of a short segment (8-16 measures) of your composition, including:
      - Time signature
      - Key signature
      - Tempo
      - Melody: Describe the notes, their durations, and how they relate to the {t['concept']}
      - Harmony: Describe the chord progressions and how they relate to the {t['concept']}
      - Rhythm: Describe the rhythmic patterns and how they relate to the {t['concept']}
   d) An explanation of the artistic choices you made and how they relate to the mathematical concept

4. Algorithmic Approach (200-250 words):
   Propose an algorithmic approach to generate music based on the {t['concept']}. Include:
   a) A high-level description of the algorithm
   b) An explanation of how it incorporates the mathematical concept
   c) A brief pseudocode snippet (5-10 lines) illustrating a key part of the algorithm

5. Cross-Domain Applications (150-200 words):
   Discuss potential applications of your approach to mathematical music composition in other fields, such as:
   a) Data sonification for scientific research
   b) Generative art or interactive installations
   c) Music therapy or cognitive enhancement

Ensure your response demonstrates a deep understanding of both music theory and the given mathematical concept. Be creative in your approach while maintaining mathematical and musical coherence. Use appropriate terminology from music theory and mathematics, providing clear explanations where necessary.

Format your response with clear headings for each section, numbered 1-5 as outlined above. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear and accurate understanding of the {t['concept']} and its application to music composition.",
            "The analysis of the existing composition is thorough, insightful, and correctly identifies mathematical patterns in music, providing specific examples.",
            "The original composition outline creatively and accurately incorporates the given mathematical concept into musical elements, with a detailed description of a short segment that clearly demonstrates the concept's application.",
            "The proposed algorithmic approach is logically sound, demonstrates an understanding of both the mathematical concept and music generation, and includes a relevant pseudocode snippet.",
            "The cross-domain applications are innovative, well-reasoned, and demonstrate a clear understanding of how the mathematical music composition approach could be applied in other fields.",
            "The response uses appropriate and advanced music theory and mathematical terminology throughout, demonstrating expertise in both domains.",
            "The response adheres to the specified word counts for each section and the overall limit, and follows the required format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
