class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"music_piece": "C D E F G A B C", "criteria": "Generate a new melody using the C major scale and include at least one instance of an ascending and descending arpeggio."},
            "2": {"music_piece": "E F# G# A B C# D# E", "criteria": "Generate a new melody using the E major scale and include a sequence of eighth notes followed by a quarter note."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following musical piece and generate a new melody based on the specified criteria:

Musical Piece: {t["music_piece"]}
Criteria: {t["criteria"]}

Ensure that the new melody follows the given criteria and adheres to the rules of music theory. Provide the new melody as a plain text string of notes separated by spaces. Format your response as follows:

New Melody: [Your new melody]

Example:
For the musical piece 'C D E F G A B C' with the criteria 'Include at least one instance of an ascending and descending arpeggio,' a suitable melody could be 'C E G C B G E C'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The new melody should follow the given musical scale.",
            "The new melody should include the specified musical elements (e.g., arpeggios, note sequences).",
            "The new melody should adhere to the rules of music theory.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
