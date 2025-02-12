class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"constraints": "Compose a short piece of music (8-16 bars) in a major key, using a 4/4 time signature, and incorporating a melody with at least two variations and chords. Include a dynamic contrast, a modulation to a different key, a ii-V-I chord progression, and a syncopated rhythmic pattern. Use a rondo form (ABACA)."},
            "2": {"analysis": "Analyze the following musical piece: 'Twinkle, Twinkle, Little Star'. Discuss the key, time signature, melody, harmony, structure, notable musical techniques used in the piece, historical context, the composer's intent, emotional expression, and the use of motifs."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'constraints' in t:
            return f"""Your task is to compose a short piece of music based on the following constraints:

Constraints: {t['constraints']}

Your composition should include:
1. A melody that fits within the given key and time signature.
2. Chords that harmonize with the melody, including a ii-V-I progression.
3. At least two variations of the melody.
4. A modulation to a different key.
5. Dynamic contrasts (e.g., changes in volume or intensity).
6. A syncopated rhythmic pattern.
7. A clear structure in rondo form (ABACA).

Provide your composition in plain text format, using standard musical notation (e.g., ABC notation)."""
        else:
            return f"""Your task is to analyze the following musical piece:

Piece: {t['analysis']}

Your analysis should include:
1. The key and time signature of the piece.
2. A discussion of the melody and harmony.
3. An explanation of the structure (e.g., verse-chorus, ABA).
4. An explanation of any notable musical techniques used in the piece (e.g., modulation, dynamics).
5. The historical context of the piece.
6. The composer's intent and any relevant background information.
7. The emotional expression conveyed by the piece.
8. The use of motifs and their development.

Provide your analysis in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'constraints' in t:
            criteria = ["The composition should adhere to the given constraints and be musically coherent."]
        else:
            criteria = ["The analysis should accurately identify the key and time signature, provide a clear discussion of the melody and harmony, explain the structure, mention any notable techniques, include historical context, the composer's intent, emotional expression, and the use of motifs."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
