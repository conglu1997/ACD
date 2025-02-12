import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "musical_concept": "chord progression",
                "mathematical_operation": "modular arithmetic",
                "linguistic_structure": "conditional statements"
            },
            {
                "musical_concept": "rhythmic pattern",
                "mathematical_operation": "Fibonacci sequence",
                "linguistic_structure": "parallel sentence structure"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze a musical {t['musical_concept']} using the mathematical concept of {t['mathematical_operation']}, then describe the results using {t['linguistic_structure']}. Your response should include the following sections:

1. Musical Analysis (200-250 words):
   a) Choose a specific example of a {t['musical_concept']} from any genre of music.
   b) Explain the basic structure and characteristics of this {t['musical_concept']}.
   c) Describe how this {t['musical_concept']} contributes to the overall composition.

2. Mathematical Transformation (250-300 words):
   a) Explain the concept of {t['mathematical_operation']} and its basic principles.
   b) Apply {t['mathematical_operation']} to your chosen {t['musical_concept']}. Describe your process step-by-step.
   c) Analyze how this mathematical transformation affects the musical properties of the original {t['musical_concept']}.

3. Linguistic Description (200-250 words):
   a) Describe the key features of {t['linguistic_structure']}.
   b) Using {t['linguistic_structure']}, create a detailed description of your mathematically transformed {t['musical_concept']}.
   c) Explain how the use of {t['linguistic_structure']} enhances or challenges the representation of your musical-mathematical analysis.

4. Interdisciplinary Insights (150-200 words):
   a) Discuss how this exercise reveals connections between music, mathematics, and language.
   b) Propose a potential application of this interdisciplinary approach in music education, composition, or analysis.

5. Creative Extension (150-200 words):
   a) Suggest a new musical piece or section based on your transformed {t['musical_concept']}.
   b) Explain how this new piece incorporates elements from all three disciplines (music, math, and linguistics).

Ensure your response demonstrates a deep understanding of musical theory, mathematical concepts, and linguistic structures. Use appropriate terminology from each field and provide clear explanations where necessary. Be creative in your approach while maintaining logical consistency across the disciplines.

Format your response with clear headings for each section. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The Musical Analysis section correctly explains a {t['musical_concept']} and its role in a composition.",
            f"The Mathematical Transformation section accurately describes {t['mathematical_operation']} and applies it to the chosen {t['musical_concept']}.",
            f"The Linguistic Description section uses {t['linguistic_structure']} effectively to describe the transformed {t['musical_concept']}.",
            "The Interdisciplinary Insights section provides meaningful connections between music, mathematics, and language.",
            "The Creative Extension section proposes a novel musical piece incorporating elements from all three disciplines.",
            "The response demonstrates a deep understanding and creative application of concepts from music theory, mathematics, and linguistics.",
            "The response follows the specified format and is between 950-1200 words in total length."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
