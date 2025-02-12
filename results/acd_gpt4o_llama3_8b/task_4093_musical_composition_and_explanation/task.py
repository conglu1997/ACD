class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"constraints": "Compose an 8-bar melody in C major, using only quarter notes and eighth notes. Include at least one instance of a repeating motif. Ensure the melody starts and ends on the tonic note (C)."},
            "2": {"constraints": "Compose an 8-bar melody in A minor, using a mix of quarter notes, eighth notes, and half notes. Include a descending melodic sequence. Ensure the melody starts and ends on the tonic note (A)."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        constraints = t['constraints']
        return f"""Generate a short musical composition based on the following constraints:

Constraints: {constraints}

Provide the musical notation for your composition using standard musical notation symbols in ASCII or plain text format. For example, you can use the following format:

C4 E4 G4 E4 | F4 D4 C4 C4 | C4 G4 E4 E4 | D4 F4 G4 C4

Ensure your composition strictly follows the given constraints. Be sure to:
- Use only the specified note values (quarter notes and eighth notes for Task 1, and quarter notes, eighth notes, and half notes for Task 2).
- Include a repeating motif in Task 1 or a descending melodic sequence in Task 2.
- Start and end the melody on the tonic note (C for Task 1, A for Task 2).

Then, provide a detailed explanation of the choices you made in your composition, including the structure, motifs, and any harmonic or melodic decisions. Ensure your explanation is logically structured and covers all aspects of your composition. Submit your response as a plain text string in the following format:

Composition: [Your musical notation]
Explanation: [Your detailed explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The composition should adhere to the given constraints.",
            "The explanation should be detailed and cover the structure, motifs, and any harmonic or melodic decisions.",
            "The musical notation should be clear and use standard symbols.",
            "The composition should start and end on the tonic note.",
            "The composition should include a repeating motif or descending melodic sequence as specified."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
