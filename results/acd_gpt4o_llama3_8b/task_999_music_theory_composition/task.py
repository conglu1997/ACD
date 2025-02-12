class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"constraints": "Compose a 4-bar melody in C major, using only quarter notes and eighth notes. The melody should start and end on the tonic (C). Use standard musical notation with letters and note lengths (e.g., C4/4 E4/8 G4/4 A4/8)."},
            "2": {"constraints": "Compose a 4-bar chord progression in the key of G major using the chords I, IV, V, and vi. The progression should follow a common cadence pattern and be suitable for a pop song. Use standard musical notation with letters and chord symbols (e.g., G, C, D, Em)."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        constraints = t["constraints"]
        return f"""Compose a short musical piece based on the following music theory constraints:\n\n{constraints}\n\nSubmit your composition as a plain text string in the following format:\n\nComposition: [Your composition here]\n\nEnsure that your composition adheres to the given constraints and is written in standard musical notation using letters (e.g., C4/4 E4/8 G4/4 A4/8 for melody or G, C, D, Em for chords)."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The composition should adhere to the specified constraints.",
            "The composition should be written in standard musical notation using letters and note lengths.",
            "The composition should be musically coherent and follow the rules of music theory."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
