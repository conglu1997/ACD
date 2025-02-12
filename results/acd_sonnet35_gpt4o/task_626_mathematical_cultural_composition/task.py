import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sequences = [
            {"name": "Fibonacci", "first_terms": [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]},
            {"name": "Prime", "first_terms": [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]}
        ]
        cultures = ["Ancient Greek", "Classical Indian", "Renaissance European", "Traditional Japanese"]
        
        return {
            "1": {"sequence": sequences[0], "culture": random.choice(cultures)},
            "2": {"sequence": sequences[1], "culture": random.choice(cultures)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Compose a musical piece based on the {t['sequence']['name']} sequence and elements from {t['culture']} culture. Your task has the following parts:

1. Composition Description (200-250 words):
   a) Describe how you would use the {t['sequence']['name']} sequence (first terms: {t['sequence']['first_terms']}) to structure your composition.
   b) Explain how you incorporate elements from {t['culture']} culture into your piece.
   c) Discuss the overall mood, tempo, and style of your composition.

2. Musical Analysis (150-200 words):
   a) Analyze the mathematical properties of your composition.
   b) Explain how the sequence influences the rhythm, melody, or harmony.
   c) Discuss any interesting patterns or structures that emerge from using this sequence.

3. Cultural Significance (150-200 words):
   a) Explain the cultural elements you've incorporated and their significance.
   b) Discuss how your composition reflects or reinterprets traditional aspects of {t['culture']} music.
   c) Consider how your piece might be received by audiences familiar with this culture.

4. Interdisciplinary Connections (100-150 words):
   Briefly explain how your composition integrates concepts from mathematics, music theory, and cultural studies.

5. Potential Variations (100-150 words):
   Propose two variations of your composition that explore different aspects of the sequence or cultural elements.

Ensure your response demonstrates a deep understanding of musical composition, mathematical sequences, and the specified culture. Be creative in your approach while maintaining musical and cultural authenticity. Use appropriate terminology from music theory and mathematics throughout your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The composition clearly incorporates the {t['sequence']['name']} sequence in its structure.",
            f"The piece integrates authentic elements from {t['culture']} culture.",
            "The response includes all required components: composition description, musical analysis, cultural significance, interdisciplinary connections, and potential variations.",
            "The analysis demonstrates a deep understanding of both mathematical and musical concepts.",
            "The composition shows creativity while maintaining musical and cultural plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
