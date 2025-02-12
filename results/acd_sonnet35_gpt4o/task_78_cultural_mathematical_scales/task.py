import random
from typing import List

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mathematical_sequences = [
            {"name": "Fibonacci", "sequence": [1, 1, 2, 3, 5, 8, 13, 21]},
            {"name": "Prime", "sequence": [2, 3, 5, 7, 11, 13, 17, 19]},
            {"name": "Triangular", "sequence": [1, 3, 6, 10, 15, 21, 28, 36]}
        ]
        
        musical_traditions = [
            "Indian Classical",
            "Chinese Pentatonic",
            "Arabic Maqam",
            "Western 12-tone",
            "African Polyrhythmic"
        ]
        
        tasks = {}
        for i in range(1, 3):
            sequence = random.choice(mathematical_sequences)
            tradition = random.choice(musical_traditions)
            tasks[str(i)] = {"sequence": sequence, "tradition": tradition}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Analyze the {t['sequence']['name']} sequence ({t['sequence']['sequence']}) in the context of {t['tradition']} music. Then, create a novel musical scale based on this analysis. Your task is to:\n\n1. Explain how the {t['sequence']['name']} sequence could be interpreted in a musical context (2-3 sentences).\n2. Describe key characteristics of {t['tradition']} music, focusing on its scale structure and intervallic relationships (3-4 sentences).\n3. Create a new musical scale that combines elements of the {t['sequence']['name']} sequence and {t['tradition']} music. Describe its structure, including the number of notes and their relationships (4-5 sentences).\n4. Provide a symbolic representation of your scale (e.g., as scale degrees, ratios, or using a notation system appropriate to the tradition).\n5. Explain how your scale reflects both the mathematical sequence and the musical tradition (3-4 sentences).\n6. Describe a potential application of your scale in contemporary music composition or music theory research (2-3 sentences).\n\nEnsure your response is creative yet grounded in both mathematical and musical principles. Organize your answer using clear headings for each section."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates understanding of both the mathematical sequence and the musical tradition",
            "The created scale logically combines elements from both the sequence and the tradition",
            "The explanation is clear, coherent, and shows interdisciplinary thinking",
            "The symbolic representation of the scale is provided and consistent with the description",
            "The potential application is creative and relevant to contemporary music or research"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0