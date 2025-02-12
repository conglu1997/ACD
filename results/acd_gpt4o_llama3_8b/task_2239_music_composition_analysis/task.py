class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "constraints": "Compose a short piece of music (approximately 8 bars) in C Major, using a 4/4 time signature. The piece should include at least one chord change and one repeated motif.",
                "analysis": "Analyze the following short piece of music and describe its key, time signature, chord progression, and any notable motifs.\n\nPiece:\nC - G - Am - F - C - G - Am - F\n"
            },
            "2": {
                "constraints": "Compose a short piece of music (approximately 8 bars) in A Minor, using a 3/4 time signature. The piece should include a modulation to a related key and at least one instance of syncopation.",
                "analysis": "Analyze the following short piece of music and describe its key, time signature, chord progression, and any notable motifs.\n\nPiece:\nAm - E - Dm - G - Am - E - Dm - G\n"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following tasks based on the given constraints and analysis instructions:

Constraints:
{t['constraints']}

Your task is to:
1. Compose a short piece of music based on the given constraints. Describe the piece in terms of its key, time signature, chord progression, and any notable motifs. Use a textual representation of the chords (e.g., 'C - G - Am - F').
2. Analyze the provided piece of music and describe its key, time signature, chord progression, and any notable motifs.

Submit your response as a plain text string in the following format:
- Composition: [Your composition description here]
- Analysis: [Your analysis here]

Ensure that your response is well-structured, coherent, and demonstrates a deep understanding of musical concepts and the provided constraints.

Example Response Format:
- Composition: Key: C Major, Time Signature: 4/4, Chord Progression: C - G - Am - F, Notable Motifs: Repeated motif in bars 1-2.
- Analysis: Key: C Major, Time Signature: 4/4, Chord Progression: C - G - Am - F - C - G - Am - F, Notable Motifs: Repeated chord progression."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The composition should adhere to the given constraints.",
            "The analysis should accurately describe the key, time signature, chord progression, and notable motifs of the provided piece.",
            "The response should be well-structured, coherent, and demonstrate a deep understanding of musical concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
