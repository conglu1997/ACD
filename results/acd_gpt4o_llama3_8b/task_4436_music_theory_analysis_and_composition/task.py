class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"composition": "C4 E4 G4 C5 C4 E4 G4 C5 G4 B4 D5 G5 E4 G4 B4 E5", "prompt": "Analyze the given musical composition and describe its harmonic structure."},
            "2": {"criteria": "Create a 4-bar melody in the key of C major using quarter notes.", "prompt": "Compose a musical piece based on the given criteria."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "composition" in t:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Composition:
{t["composition"]}

Your analysis should include:
1. Identification of the key and chords used.
2. Description of the harmonic structure, including any chord progressions.
3. Any notable features or patterns, such as motifs, repetitions, or variations.
4. An explanation of how the harmonic structure contributes to the overall musical expression.

Ensure your analysis is coherent, well-structured, and based on music theory principles. Submit your response as a plain text string in paragraph format."""
        else:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Criteria:
{t["criteria"]}

Your composition should include:
1. A 4-bar melody in the key of C major.
2. Use only quarter notes.
3. Ensure the melody is coherent, follows basic music theory principles, and includes at least one repetition or motif.
4. Provide a brief explanation of how you structured the melody and why.

Submit your composition as a plain text string in the following format:
[Note sequence]

For example: C4 E4 G4 C5 C4 E4 G4 C5 G4 B4 D5 G5 E4 G4 B4 E5

Explanation: [Your explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "composition" in t:
            criteria = ["The analysis should identify the key and chords used.", "The description should cover the harmonic structure, including any chord progressions.", "The analysis should mention notable features or patterns, such as motifs, repetitions, or variations.", "The explanation should describe how the harmonic structure contributes to the overall musical expression."]
        else:
            criteria = ["The composition should be a 4-bar melody in the key of C major.", "Only quarter notes should be used.", "The melody should be coherent, follow basic music theory principles, and include at least one repetition or motif.", "The explanation should describe how the melody was structured and why."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
