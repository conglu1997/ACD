import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mathematical_sequences = [
            "Fibonacci sequence",
            "Prime numbers",
            "Pascal's triangle",
            "Geometric sequence",
            "Catalan numbers"
        ]
        cultural_contexts = [
            "Ancient Mayan civilization",
            "Contemporary urban Japan",
            "Nomadic Mongolian tribe",
            "Renaissance-era Venice",
            "Futuristic Mars colony"
        ]
        return {
            "1": {
                "sequence": random.choice(mathematical_sequences),
                "context": random.choice(cultural_contexts)
            },
            "2": {
                "sequence": random.choice(mathematical_sequences),
                "context": random.choice(cultural_contexts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel musical scale based on the {t['sequence']}, then analyze its potential cultural impact if adopted by {t['context']}. Your response should include:

1. Mathematical Foundation (150-200 words):
   a) Explain how you will use the {t['sequence']} to generate your musical scale.
   b) Provide the first 8 notes of your scale, showing your step-by-step calculations.
   c) Describe any unique properties of your scale derived from the mathematical sequence.
   d) Provide a detailed textual description of how your scale would be visually represented (e.g., on a musical staff or alternative notation system).

2. Musical Analysis (200-250 words):
   a) Compare your scale to traditional Western scales (e.g., major, minor, pentatonic).
   b) Discuss the potential harmonic and melodic implications of your scale.
   c) Propose a simple musical motif or phrase that showcases the unique qualities of your scale.

3. Cultural Impact Analysis (250-300 words):
   a) Briefly describe the musical traditions and cultural values of {t['context']}.
   b) Analyze how the adoption of your scale might influence the music and broader culture of this society.
   c) Discuss potential challenges or resistance to adopting this new scale.
   d) Propose one way this scale could be integrated into an existing cultural practice or ceremony.

4. Interdisciplinary Connections (150-200 words):
   Explore how this musical-mathematical fusion might influence or be applied to another field (e.g., architecture, visual arts, linguistics, or social structures) within the given cultural context.

Ensure your response demonstrates a deep understanding of music theory, mathematical sequences, and cultural analysis. Be creative in your approach while maintaining logical consistency and plausibility within the given context. Explain any technical terms or concepts you use. Your total response should be between 750-1000 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The musical scale is clearly based on the {t['sequence']}.",
            "The first 8 notes of the scale are provided with step-by-step calculations.",
            "A detailed textual description of the scale's visual representation is included.",
            "The scale is compared to traditional Western scales.",
            "A simple musical motif or phrase is proposed using the new scale.",
            f"The cultural impact analysis considers the specific context of {t['context']}.",
            "The response explores interdisciplinary connections beyond music and mathematics.",
            "The response includes all four required sections: Mathematical Foundation, Musical Analysis, Cultural Impact Analysis, and Interdisciplinary Connections.",
            "Technical terms and concepts are explained clearly.",
            "The total response is between 750-1000 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
