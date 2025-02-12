import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mathematical_concepts = [
            {
                "concept": "Fourier Transform",
                "description": "A mathematical transform that decomposes functions depending on space or time into functions depending on spatial or temporal frequency"
            },
            {
                "concept": "Fibonacci Sequence",
                "description": "A sequence of numbers in which each number is the sum of the two preceding ones"
            },
            {
                "concept": "Mandelbrot Set",
                "description": "A set of complex numbers that remain bounded under a specific mathematical operation"
            },
            {
                "concept": "Riemann Hypothesis",
                "description": "A conjecture about the distribution of prime numbers and complex zeros of the Riemann zeta function"
            }
        ]
        return {str(i+1): concept for i, concept in enumerate(random.sample(mathematical_concepts, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel musical notation system that encodes the mathematical concept of {t['concept']}. Your task is to:

1. Notation System Design (250-300 words):
   a) Describe the basic elements of your musical notation system (e.g., notes, scales, rhythms).
   b) Explain how these elements correspond to aspects of the {t['concept']}.
   c) Provide a visual description or example of how a simple mathematical operation within this concept would be notated.

2. Mathematical-Musical Mapping (200-250 words):
   a) Explain in detail how your notation system captures the key properties and behaviors of the {t['concept']}.
   b) Describe how mathematical operations or transformations would be represented as musical operations.
   c) Discuss any limitations or challenges in representing this concept musically.

3. Composition Task (200-250 words):
   a) Describe a short musical composition that represents a specific mathematical statement or operation related to the {t['concept']}.
   b) Explain how the composition's structure and elements reflect the mathematical content.
   c) Discuss how changes in the mathematical statement would be reflected in the musical piece.

4. Cognitive Implications (150-200 words):
   a) Analyze how this notation system might affect the way people think about or understand the {t['concept']}.
   b) Discuss potential applications of this system in mathematics education or research.

5. AI Interpretation Challenge (150-200 words):
   a) Propose a specific task that would test an AI's ability to interpret and manipulate mathematical ideas using your notation system.
   b) Describe what successful completion of this task would demonstrate about the AI's capabilities.

Ensure your response demonstrates a deep understanding of both music theory and the specified mathematical concept. Be creative in your design while maintaining mathematical accuracy and musical plausibility. Your total response should be between 950-1200 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a coherent description of a musical notation system that encodes {t['concept']}",
            "The mathematical-musical mapping is logically consistent and captures key aspects of the concept",
            "The composition task demonstrates a clear application of the notation system to represent mathematical ideas",
            "The cognitive implications and AI interpretation challenge are thoughtfully considered and relevant",
            "The overall response demonstrates deep understanding of both music theory and the specified mathematical concept",
            "The design is creative while maintaining mathematical accuracy and musical plausibility",
            "The response follows the specified format and is within the 950-1200 word limit"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
