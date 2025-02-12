import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sequences = [
            {
                "name": "Fibonacci sequence",
                "first_10_terms": [0, 1, 1, 2, 3, 5, 8, 13, 21, 34],
                "transformation": "Square each term"
            },
            {
                "name": "Prime number sequence",
                "first_10_terms": [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
                "transformation": "Subtract each term from the next prime number"
            }
        ]
        return {
            "1": random.choice(sequences),
            "2": random.choice(sequences)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following mathematical sequence and create a musical composition based on it:

Sequence: {t['name']}
First 10 terms: {t['first_10_terms']}

Your task has three parts:

1. Sequence Analysis (100-150 words):
   a) Describe the key properties of the sequence.
   b) Explain how the sequence grows or changes.
   c) Identify any patterns or relationships between terms.

2. Musical Translation (200-250 words):
   Create a musical composition based on the sequence using these parameters:
   - Assign each unique term in the sequence to a note in the C major scale (C, D, E, F, G, A, B).
   - Use the position of each term in the sequence to determine its duration (e.g., 1st term = whole note, 2nd term = half note, etc.).
   - Describe how you would arrange these notes into a cohesive musical piece, including:
     * Melody: How the main tune would sound based on the sequence.
     * Harmony: Suggest chord progressions that complement the melody.
     * Rhythm: Describe any recurring rhythmic patterns based on the sequence.
     * Structure: Outline the overall form of the piece (e.g., ABA, verse-chorus, etc.).
   Explain your choices and how they relate to the mathematical properties of the sequence.

3. Mathematical Transformation and Variation (150-200 words):
   Apply the following transformation to the original sequence: {t['transformation']}
   a) Show the first 5 terms of the transformed sequence.
   b) Describe how you would modify your musical composition to reflect this transformation.
   c) Explain how this change affects the musical properties (melody, harmony, rhythm, structure) of your piece.

Ensure your response demonstrates a deep understanding of both mathematical concepts and music theory principles. Be creative in your musical interpretations while maintaining a clear connection to the underlying mathematical sequence."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The sequence analysis accurately describes the properties and patterns of the given mathematical sequence.",
            "The musical translation demonstrates a clear and creative mapping of the sequence to musical elements (notes, durations, etc.).",
            "The composition description includes all required elements: melody, harmony, rhythm, and structure.",
            "The mathematical transformation is correctly applied and clearly explained.",
            "The variation of the musical piece based on the transformed sequence is logically described and consistent with the original composition.",
            "The response shows a deep understanding of both mathematical concepts and music theory principles.",
            "The overall response is creative, coherent, and demonstrates strong interdisciplinary thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
