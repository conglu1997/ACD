class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "instructions": "Generate musical notation for a simple melody in C major. The melody should be 4 bars long, in 4/4 time, and include a variety of quarter notes, half notes, and whole notes. Submit your notation in ABC notation format. ABC notation is a text-based way of representing music, where each letter corresponds to a note (e.g., C, D, E, F, G, A, B), and symbols like '|' represent bar lines. For example, a 4/4 bar with quarter notes could be represented as 'C D E F |'. Do not include the answer in your response."
            },
            "2": {
                "instructions": "Convert the following description into musical notation in ABC notation format. The piece should be in G major, 3/4 time, 8 bars long, and include a mix of eighth notes and quarter notes. Description: 'A lively waltz that starts with G and ascends to D before descending back to G in the first four bars. The second four bars should mirror this pattern but start from D and descend to G, then back up to D.' ABC notation is a text-based way of representing music, where each letter corresponds to a note (e.g., G, A, B, c, d, e, f, g), and symbols like '|' represent bar lines. For example, a 3/4 bar with quarter notes could be represented as 'G A B |'. Do not include the answer in your response."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return t["instructions"]

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The submission should be in ABC notation format.",
            "The submission should be musically valid and follow the given instructions regarding key, time signature, length, and note types.",
            "The submission should not include the example or any direct hints given in the instructions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
