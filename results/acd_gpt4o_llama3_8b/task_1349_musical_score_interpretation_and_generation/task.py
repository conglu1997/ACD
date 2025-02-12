class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"input_score": "C4 E4 G4 C5 | D4 F4 A4 D5 | E4 G4 B4 E5", "generation_criteria": "Compose a continuation of this melody in a similar style, maintaining the same key, rhythmic pattern, and dynamics."},
            "2": {"input_score": "A2 B2 C3 D3 | E3 F3 G3 A3 | B3 C4 D4 E4", "generation_criteria": "Compose a harmony for this melody that complements it, using the same key, similar rhythmic pattern, and appropriate dynamics."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Interpret the given musical score and complete the associated task based on the specified criteria:\nInput Score: {t['input_score']}\nGeneration Criteria: {t['generation_criteria']}\nYour response should include:\n1. An interpretation of the input score, explaining the musical elements present (e.g., notes, rhythm, key, tempo, dynamics).\n2. A new composition that meets the generation criteria.\n\nExample Interpretation:\nNotes: C4, E4, G4, C5\nRhythm: Quarter notes\nKey: C Major\nTempo: Moderato\nDynamics: Mezzo-forte\n\nSubmit your response as a plain text string in the following format:\n\nInterpretation: [Your interpretation]\nComposition: [Your composition]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The interpretation should accurately explain the musical elements of the input score (notes, rhythm, key, tempo, dynamics).", "The composition should be musically coherent, maintain the same key, rhythmic pattern, and dynamics, and meet the generation criteria."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
