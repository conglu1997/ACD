class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"requirements": "Compose a 4-bar melody in C major using quarter notes and half notes only."},
            "2": {"requirements": "Compose a 4-bar chord progression in G minor using triads."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given requirements:

Requirements: {t['requirements']}

Compose a piece of music that meets the specified requirements. Represent your composition using text notation (e.g., C4, D4, E4 for melody notes or Gm, Cm for chords). Additionally, provide a detailed explanation of your compositional choices, including the musical theory and reasoning behind your decisions. Submit your response as a plain text string with the following sections:
1. Composition: [Your musical composition]
2. Explanation: [Your detailed explanation covering the musical theory, note choices, and structure]

Example format for melody composition:
Composition: C4 D4 E4 F4 | G4 A4 B4 C5 | D4 E4 F4 G4 | A4 B4 C5 D5
Explanation: The melody starts with a simple ascending pattern in C major, using quarter notes to maintain a steady rhythm. The choice of starting with C4 establishes the tonic, and the subsequent notes follow the C major scale...

Example format for chord progression composition:
Composition: Gm | Cm | Dm | Gm
Explanation: The chord progression in G minor starts with the tonic (G minor), followed by the subdominant (C minor), moving to the dominant (D minor), and returning to the tonic (G minor). This progression creates a sense of resolution and cohesiveness..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a correct and functional musical composition.",
            "The response should include a detailed explanation of the compositional choices.",
            "The explanation should cover the musical theory and reasoning behind the composition.",
            "The composition should meet the specified requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
