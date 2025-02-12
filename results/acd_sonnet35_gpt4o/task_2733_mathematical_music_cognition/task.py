import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_phenomena = [
            "synesthesia",
            "absolute pitch",
            "musical memory",
            "emotional responses to music"
        ]
        mathematical_concepts = [
            "Fibonacci sequence",
            "prime numbers",
            "fractal geometry",
            "modular arithmetic"
        ]
        tasks = {
            "1": {
                "cognitive_phenomenon": random.choice(cognitive_phenomena),
                "mathematical_concept": random.choice(mathematical_concepts)
            },
            "2": {
                "cognitive_phenomenon": random.choice(cognitive_phenomena),
                "mathematical_concept": random.choice(mathematical_concepts)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel musical system based on the mathematical concept of {t['mathematical_concept']}, then use it to explore and explain the cognitive phenomenon of {t['cognitive_phenomenon']}. Your response should include:

1. Mathematical Foundation (250-300 words):
   a) Explain the key aspects of {t['mathematical_concept']} relevant to your musical system.
   b) Describe how you will translate this mathematical concept into musical elements (e.g., pitch, rhythm, harmony).
   c) Provide at least one example of how a mathematical operation in your system translates to a musical operation.

2. Musical System Design (300-350 words):
   a) Define the basic elements of your musical system (e.g., notes, scales, rhythmic units).
   b) Explain the rules or algorithms for generating melodies or harmonies in your system.
   c) Describe how your system differs from traditional Western music theory.
   d) Provide a short musical phrase or pattern (using standard notation, tablature, or a clear textual description) that exemplifies your system.

3. Cognitive Phenomenon Analysis (250-300 words):
   a) Briefly explain the key features of {t['cognitive_phenomenon']}.
   b) Describe how your musical system could be used to explore or explain this phenomenon.
   c) Propose a specific experiment or study using your system to investigate {t['cognitive_phenomenon']}.

4. Interdisciplinary Connections (200-250 words):
   a) Discuss how your musical system bridges mathematics, music theory, and cognitive science.
   b) Explain any novel insights or hypotheses about {t['cognitive_phenomenon']} that arise from your system.
   c) Propose how your system might be used in other fields (e.g., education, therapy, artificial intelligence).

5. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations or challenges in your musical system or its application to {t['cognitive_phenomenon']}.
   b) Suggest ways to address these limitations or expand upon your system in future research.

Ensure your response demonstrates a deep understanding of mathematics, music theory, and cognitive science. Use appropriate terminology from each field and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and logical consistency.

Format your answer with clear headings for each section. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['mathematical_concept']} and how it can be applied to music",
            "The musical system design is novel, coherent, and well-explained",
            f"The analysis of {t['cognitive_phenomenon']} is accurate and insightfully connected to the musical system",
            "The proposed experiment or study is well-designed and relevant",
            "The response shows creative problem-solving and interdisciplinary knowledge integration",
            "The limitations and future directions are thoughtfully considered",
            "The answer is well-structured, coherent, and adheres to the specified word count"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
