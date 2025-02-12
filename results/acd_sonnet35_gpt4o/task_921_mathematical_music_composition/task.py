import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"mathematical_concept": "Fibonacci sequence", "musical_style": "Minimalism"},
            "2": {"mathematical_concept": "Fractal geometry", "musical_style": "Jazz"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel musical composition system that integrates the mathematical concept of {t['mathematical_concept']} with the musical style of {t['musical_style']}. Then use this system to compose a short piece of music. Your response should include:

1. Concept Explanations (100-150 words):
   a) Briefly explain the chosen mathematical concept ({t['mathematical_concept']}).
   b) Provide a short description of the musical style ({t['musical_style']}).

2. System Design (250-300 words):
   a) Explain how your composition system incorporates {t['mathematical_concept']}.
   b) Describe how it reflects the characteristics of {t['musical_style']}.
   c) Detail the key components and rules of your system.

3. Mathematical Representation (100-150 words):
   Provide a mathematical formula or algorithm that represents a core aspect of your composition system. Use standard mathematical notation and include a brief explanation of each variable or function.

4. Musical Notation (100-150 words):
   Describe how your system translates mathematical concepts into musical elements (e.g., pitch, rhythm, harmony).

5. Composition Process (200-250 words):
   a) Outline the steps you would take to compose a piece using your system.
   b) Explain any choices or interpretations made during the composition process.

6. Sample Composition (150-200 words):
   Provide a written description of a short (30-60 second) piece composed using your system. Include details about its structure, key musical elements, and how it reflects both the mathematical concept and musical style.

7. Analysis (200-250 words):
   a) Discuss how your system and composition reflect the integration of mathematics and music.
   b) Analyze the potential artistic and mathematical implications of your approach.
   c) Consider how this system might be perceived by musicians and mathematicians.

8. Potential Applications (100-150 words):
   Suggest two potential applications or extensions of your system in music education, composition, or mathematical research.

Ensure your response demonstrates a deep understanding of both the chosen mathematical concept and musical style. Be creative in your system design while maintaining mathematical and musical integrity. Your total response should be between 1200-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes clear explanations of {t['mathematical_concept']} and {t['musical_style']}.",
            f"The composition system clearly integrates {t['mathematical_concept']} with {t['musical_style']}.",
            "The mathematical representation is valid, relevant to the system design, and properly explained.",
            "The musical notation method is clearly explained and logically connects mathematics to musical elements.",
            "The composition process is well-defined and demonstrates how the system is used.",
            "The sample composition description reflects both the mathematical concept and musical style.",
            "The analysis shows insight into the integration of mathematics and music.",
            "The potential applications are creative and relevant to music or mathematics.",
            "The overall response demonstrates a deep understanding of music theory and mathematics."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
