class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "compose", "constraints": "Compose a short melody in C major using only quarter notes and eighth notes. The melody should be 8 bars long and written in 4/4 time signature."},
            "2": {"task_type": "explain", "question": "Explain the concept of a 'chord progression' and provide an example of a common chord progression in Western music."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "compose":
            instructions = f"""Your task is to compose a short musical melody based on the following constraints:

Constraints: {t['constraints']}

Provide the melody in a textual format using standard musical notation symbols (e.g., C4 for middle C, D4 for the D above middle C). Use the following format to indicate the rhythm:
- Quarter notes: C4
- Eighth notes: C4-E4

Ensure the melody adheres to the given constraints, is musically coherent, and follows a 4/4 time signature. Here is an example of how your response should look:

Melody: C4 D4 E4 F4 | G4 A4 B4 C5 | E4 D4 C4 G4 | A4 B4 C5 D5 | E4 F4 G4 A4 | B4 C5 D5 E5 | F4 E4 D4 C4 | B4 A4 G4 F4

Your melody should be 8 bars long, use only quarter notes and eighth notes, and be written in 4/4 time signature."""
        else:
            instructions = f"""Your task is to explain a fundamental concept in musical theory and provide an example. Here is the question:

Question: {t['question']}

Provide your explanation in plain text format. Ensure that your explanation is clear, detailed, and includes an example to illustrate the concept. Here is an example of how your response should look:

Response: A chord progression is a sequence of chords played in succession. A common chord progression in Western music is the I-IV-V-I progression, which consists of the tonic, subdominant, dominant, and tonic chords. For example, in the key of C major, this progression would be C major, F major, G major, and C major."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "compose":
            criteria = ["The melody should be in C major.", "The melody should be 8 bars long.", "The melody should use only quarter notes and eighth notes.", "The melody should be musically coherent.", "The melody should follow a 4/4 time signature."]
        else:
            criteria = ["The explanation should correctly describe the concept of a chord progression.", "The example provided should be accurate and relevant.", "The explanation should be clear and detailed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
