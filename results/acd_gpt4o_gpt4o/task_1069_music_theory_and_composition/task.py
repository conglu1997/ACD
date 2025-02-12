class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_type": "composition",
                "constraints": "4/4 time signature, key of C major, must include a melody and harmony, at least 16 bars"
            },
            "2": {
                "task_type": "analysis",
                "music_piece": "C E G C E G | A C E A C E | F A C F A C | G B D G B D"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'composition':
            return f"""Your task is to compose a piece of music based on the following constraints:

Constraints: {t['constraints']}

Provide your composition in plain text format using standard musical notation (e.g., C D E F G A B C for melody and corresponding chords for harmony). Clearly separate the melody and harmony lines.

Expected format:
Melody: [Your melody]
Harmony: [Your harmony]
"""
        elif t['task_type'] == 'analysis':
            return f"""Your task is to analyze the following piece of music and identify its theoretical elements:

Piece: {t['music_piece']}

Identify the following elements:
1. Key
2. Chord progressions
3. Time signature

Provide your analysis in plain text format.

Expected format:
Key: [Your identified key]
Chord Progressions: [Your identified chord progressions]
Time Signature: [Your identified time signature]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'composition':
            criteria = [
                "The composition should be in 4/4 time signature.",
                "The composition should be in the key of C major.",
                "The composition should include both melody and harmony.",
                "The composition should be at least 16 bars long."
            ]
        elif t['task_type'] == 'analysis':
            criteria = [
                "The analysis should correctly identify the key.",
                "The analysis should correctly identify the chord progressions.",
                "The analysis should correctly identify the time signature."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
