import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "mathematical_concept": "Fibonacci sequence",
                "cultural_tradition": "Indian classical music (Hindustani)",
                "musical_element": "Rhythm (Tala)"
            },
            {
                "mathematical_concept": "Fractal geometry",
                "cultural_tradition": "West African polyrhythms",
                "musical_element": "Melody"
            },
            {
                "mathematical_concept": "Golden ratio",
                "cultural_tradition": "Chinese pentatonic scale",
                "musical_element": "Harmony"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a musical composition system that integrates the mathematical concept of {t['mathematical_concept']} with the cultural tradition of {t['cultural_tradition']}, focusing on the musical element of {t['musical_element']}. Then, use your system to create and analyze a short piece of music. Your response should include the following sections:

1. System Design (250-300 words):
   a) Explain how you integrate the given mathematical concept into the musical composition process.
   b) Describe how you incorporate elements from the specified cultural tradition.
   c) Detail how your system addresses the focused musical element.
   d) Provide a step-by-step process for creating a composition using your system.

2. Composition Creation (200-250 words):
   a) Use your system to create a short musical piece (describe it in words, do not provide actual musical notation).
   b) Explain how each aspect of your composition reflects the mathematical concept and cultural tradition.
   c) Discuss any challenges you encountered in the composition process and how you addressed them.

3. Musical Analysis (200-250 words):
   a) Analyze the structure and characteristics of your composition.
   b) Explain how the mathematical concept influences the overall form or progression of the piece.
   c) Discuss how elements of the cultural tradition are expressed in the composition.

4. Cultural and Mathematical Implications (150-200 words):
   a) Explore how your system might change our understanding of the relationship between mathematics and music.
   b) Discuss the potential cultural implications of fusing mathematical concepts with traditional musical forms.
   c) Propose an experiment to test whether listeners can perceive the mathematical structures in the music created by your system.

5. Potential Applications (150-200 words):
   a) Suggest two potential applications of your musical composition system in fields outside of music (e.g., education, therapy, or scientific research).
   b) Explain how these applications could benefit from the integration of mathematical concepts and cultural traditions in music.

Ensure your response demonstrates a deep understanding of music theory, mathematics, and cultural anthropology. Be creative in your approach while maintaining logical consistency and cultural sensitivity. Use clear, concise language and provide detailed explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must integrate {t['mathematical_concept']} with {t['cultural_tradition']}, focusing on {t['musical_element']}",
            "The system design should be clearly explained and logically consistent",
            "The composition creation should demonstrate the application of the designed system",
            "The musical analysis should show a deep understanding of both mathematical and cultural elements",
            "The response should explore implications and applications beyond music",
            "The overall response should demonstrate creativity, interdisciplinary knowledge, and analytical reasoning"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
