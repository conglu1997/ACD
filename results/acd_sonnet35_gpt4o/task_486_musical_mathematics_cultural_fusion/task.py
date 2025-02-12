import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mathematical_concepts = [
            {
                "name": "Fibonacci sequence",
                "description": "A sequence where each number is the sum of the two preceding ones"
            },
            {
                "name": "Golden ratio",
                "description": "A special number approximately equal to 1.618"
            },
            {
                "name": "Prime numbers",
                "description": "Natural numbers greater than 1 that are only divisible by 1 and themselves"
            },
            {
                "name": "Fractal geometry",
                "description": "Complex patterns that are self-similar across different scales"
            }
        ]
        selected_concepts = random.sample(mathematical_concepts, 2)
        return {
            "1": {"concept1": selected_concepts[0], "concept2": selected_concepts[1], "note_count": random.randint(5, 12)},
            "2": {"concept1": selected_concepts[1], "concept2": selected_concepts[0], "note_count": random.randint(5, 12)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a new musical scale based on the mathematical concepts of {t['concept1']['name']} and {t['concept2']['name']}, and analyze its potential cultural impact. Your scale must have exactly {t['note_count']} notes. Your task consists of the following parts:

1. Scale Design (200-250 words):
   a) Explain how you will use {t['concept1']['name']} and {t['concept2']['name']} to create a new musical scale.
   b) Describe the structure of your {t['note_count']}-note scale, including the relationships between notes.
   c) Compare your scale to a traditional scale (e.g., major scale, minor scale) and highlight key differences.

2. Mathematical Analysis (150-200 words):
   a) Provide a detailed mathematical explanation of how your scale incorporates both {t['concept1']['name']} and {t['concept2']['name']}.
   b) Include at least one formula or equation that demonstrates the mathematical principles behind your scale.
   c) Provide the frequency ratios between adjacent notes in your scale, rounded to four decimal places.

3. Visual Representation (requirement):
   Create a visual representation of your scale. This could be a diagram, a graph, or any other visual format that clearly illustrates the structure and mathematical relationships in your scale. Describe this visual in words, as if you were explaining it to someone who cannot see it.

4. Musical Characteristics (150-200 words):
   a) Describe the unique tonal qualities or harmonies that might emerge from your scale.
   b) Explain how these characteristics might influence melody, harmony, and rhythm in compositions using this scale.

5. Instrument Adaptation (100-150 words):
   a) Discuss how existing musical instruments might need to be modified to play your scale accurately.
   b) Propose a new instrument specifically designed for your scale, if applicable.

6. Cultural Impact Analysis (200-250 words):
   a) Speculate on how your scale might be received in different musical traditions (e.g., Western classical, Indian classical, Jazz, etc.).
   b) Discuss potential challenges in adopting this scale in various cultural contexts.
   c) Explore possible new genres or fusion styles that might emerge from the use of your scale.

7. Composition Example (100-150 words):
   Describe a short musical piece that could be composed using your scale. Explain how it would showcase the unique features of your scale and its mathematical basis. Include a textual representation of the first few measures of the piece using note names or numbers.

Ensure your response demonstrates a deep understanding of music theory, mathematical concepts, and cultural analysis. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining musical and mathematical plausibility.

Format your response with clear headings for each section, and number your paragraphs within each section for clarity."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a coherent design of a {t['note_count']}-note musical scale based on both {t['concept1']['name']} and {t['concept2']['name']}",
            "The mathematical analysis accurately applies both chosen concepts to music theory and includes correct frequency ratios",
            "A visual representation of the scale is described clearly and consistently with the mathematical principles",
            "The musical characteristics described are logically derived from the scale design",
            "The cultural impact analysis demonstrates an understanding of diverse musical traditions",
            "The composition example effectively illustrates the unique features of the designed scale and includes a textual representation of the first few measures",
            "The overall response shows creativity, interdisciplinary knowledge application, and adherence to the specified format"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
