class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "composition", "instructions": "Compose a short musical piece for a solo piano. The piece should be in a major key, have a tempo marking of Allegro, and should include at least three different chords. Submit your composition as a plain text string of musical notation in the format: Note Octave [Accidental (if any)] Duration, e.g., 'C4 quarter, D#4 half, E4 whole'."},
            "2": {"task_type": "interpretation", "score": "C4 E4 G4 | D4 F4 A4 | E4 G4 B4 | C4 E4 G4 | G4 B4 D5 | F4 A4 C5 | E4 G4 B4 | C4 E4 G4", "instructions": "Interpret the given musical score. Describe the key, tempo, and structure of the piece. Also, identify any repeating patterns or motifs. Submit your interpretation as a plain text string in the following format: \nKey: [Your answer]\nTempo: [Your answer]\nStructure: [Your answer]\nPatterns: [Your answer]"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "composition":
            return "Compose a short musical piece for a solo piano. The piece should be in a major key, have a tempo marking of Allegro, and should include at least three different chords. Submit your composition as a plain text string of musical notation in the format: Note Octave [Accidental (if any)] Duration, e.g., 'C4 quarter, D#4 half, E4 whole'."
        elif t["task_type"] == "interpretation":
            return f"Interpret the given musical score: {t['score']}. Describe the key, tempo, and structure of the piece. Also, identify any repeating patterns or motifs. Submit your interpretation as a plain text string in the following format:\nKey: [Your answer]\nTempo: [Your answer]\nStructure: [Your answer]\nPatterns: [Your answer]"
        else:
            raise ValueError("Invalid task type")

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "composition":
            criteria = [
                "The piece should be in a major key.",
                "The tempo marking should be Allegro.",
                "The piece should include at least three different chords."]
        elif t["task_type"] == "interpretation":
            criteria = [
                "The interpretation should correctly identify the key.",
                "The interpretation should correctly identify the tempo.",
                "The interpretation should correctly describe the structure.",
                "The interpretation should correctly identify repeating patterns or motifs."]
        else:
            raise ValueError("Invalid task type")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
