import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {
                "name": "Ancient Mayan",
                "mathematical_concept": "Vigesimal (base-20) number system",
                "cultural_element": "Celestial observations and calendar system"
            },
            {
                "name": "Medieval Islamic",
                "mathematical_concept": "Golden ratio",
                "cultural_element": "Geometric patterns in art and architecture"
            },
            {
                "name": "Renaissance Italian",
                "mathematical_concept": "Fibonacci sequence",
                "cultural_element": "Harmonic proportions in visual arts"
            },
            {
                "name": "Ancient Greek",
                "mathematical_concept": "Pythagorean tuning",
                "cultural_element": "Philosophical harmony of the spheres"
            }
        ]
        return {str(i+1): culture for i, culture in enumerate(random.sample(cultures, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a novel musical scale based on the {t['name']} culture, incorporating the mathematical concept of {t['mathematical_concept']} and the cultural element of {t['cultural_element']}. Then, analyze its properties and potential applications. Your response should include:

1. Scale Design (200-250 words):
   a) Describe the structure of your musical scale, including the number of notes and their relationships.
   b) Explain how you've incorporated the given mathematical concept into the scale's design.
   c) Discuss how the cultural element influences the scale's characteristics.
   d) Provide a mathematical formula or procedure for generating the frequencies of your scale.

2. Musical Analysis (200-250 words):
   a) Analyze the harmonic properties of your scale, including any unique intervals or chords it produces.
   b) Compare and contrast your scale with a traditional Western 12-tone equal temperament scale.
   c) Discuss any challenges or opportunities this scale presents for melody and harmony creation.
   d) Propose a simple musical motif or phrase that showcases the unique qualities of your scale.

3. Cultural Significance (150-200 words):
   a) Explain how your scale reflects or embodies aspects of the given culture.
   b) Discuss potential cultural or spiritual significance of the mathematical relationships in your scale.
   c) Describe how traditional instruments from this culture might be adapted to play your scale.

4. Modern Applications (150-200 words):
   a) Propose an innovative application of your scale in contemporary music composition.
   b) Discuss how your scale could be used in music therapy or sound healing practices.
   c) Describe how modern technology could be used to implement or explore your scale.

5. Interdisciplinary Connections (100-150 words):
   a) Explain how your scale demonstrates connections between mathematics, music, and culture.
   b) Discuss any insights your scale provides about the universal nature of mathematical patterns in music.
   c) Propose a potential research question or experiment inspired by your scale design.

Ensure your response demonstrates a deep understanding of music theory, mathematical principles, and cultural sensitivity. Be creative in your scale design while maintaining mathematical accuracy and cultural relevance. Your total response should be between 800-1050 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all five required sections with appropriate detail and adheres to the specified word count for each section.",
            "The scale design (200-250 words) incorporates the given mathematical concept and cultural element in a meaningful way.",
            "The musical analysis (200-250 words) demonstrates a deep understanding of music theory and the properties of the created scale.",
            "The cultural significance (150-200 words) is well-explained and relevant to the given culture.",
            "The modern applications (150-200 words) and interdisciplinary connections (100-150 words) are innovative and well-reasoned.",
            "The overall response shows creativity, mathematical accuracy, and cultural sensitivity."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
