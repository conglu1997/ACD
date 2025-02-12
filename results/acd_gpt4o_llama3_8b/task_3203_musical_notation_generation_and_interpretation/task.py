class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task": "Generate a piece of music notation",
                "parameters": {
                    "key": "C Major",
                    "time_signature": "4/4",
                    "length": "8 bars",
                    "tempo": "120 BPM"
                }
            },
            "2": {
                "task": "Interpret a piece of music notation",
                "notation": "| C4 E4 G4 C5 | D4 F4 A4 D5 | E4 G4 B4 E5 | F4 A4 C5 F5 | G4 B4 D5 G5 | A4 C5 E5 A5 | B4 D5 F#5 B5 | C5 E5 G5 C6 |"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task'] == "Generate a piece of music notation":
            params = t['parameters']
            return f"""Generate a piece of music notation based on the following parameters:

Key: {params['key']}
Time Signature: {params['time_signature']}
Length: {params['length']}
Tempo: {params['tempo']} BPM

Submit your response as a plain text string with each note represented in scientific pitch notation and separated by vertical bars for each measure.
Example: | C4 E4 G4 | D4 F4 A4 | ...
Ensure that the music is melodically and rhythmically coherent within the given parameters."""
        elif t['task'] == "Interpret a piece of music notation":
            return f"""Interpret the following piece of music notation and describe it in plain text. Include details about the key, time signature, tempo, and any noticeable patterns or structures.

Notation: {t['notation']}

Submit your response as a plain text string in the following format:
Description: [Your description]
Ensure that your interpretation is detailed and covers all the specified aspects."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task'] == "Generate a piece of music notation":
            criteria = [
                "The music notation should be in the correct key and time signature.",
                "The length of the piece should be 8 bars.",
                "The tempo should be taken into consideration in the rhythmic structure.",
                "The music should be melodically and rhythmically coherent."
            ]
        elif t['task'] == "Interpret a piece of music notation":
            criteria = [
                "The interpretation should correctly identify the key and time signature.",
                "The interpretation should mention the tempo.",
                "The interpretation should describe any noticeable patterns or structures.",
                "The interpretation should be detailed and cover all specified aspects."
            ]
        else:
            return 0.0
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
