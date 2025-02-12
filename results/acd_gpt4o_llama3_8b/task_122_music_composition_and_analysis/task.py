class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "parameters": {
                    "key": "C Major",
                    "time_signature": "4/4",
                    "length": "8 bars"
                }
            },
            "2": {
                "composition": "C D E F | G A B C | C B A G | F E D C | C E G C | D F A D | E G B E | F A C F"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "parameters" in t:
            return f"""Compose a short piece of music based on the following parameters:

Key: {t['parameters']['key']}
Time Signature: {t['parameters']['time_signature']}
Length: {t['parameters']['length']}

Ensure that the composition adheres to the given key and time signature, and is exactly 8 bars in length. Submit your composition as a plain text string in the format of musical notes, separated by spaces and bars by '|'. For example, a valid composition format would be 'C D E F | G A B C | ...'."""
        elif "composition" in t:
            return f"""Analyze the following musical composition and provide a detailed explanation of its structure, harmony, and potential emotional impact:

Composition: {t['composition']}

Your analysis should include:
1. Identification of the key and time signature.
2. Description of the harmonic progression.
3. Interpretation of the emotional impact of the piece.
4. Ensure that your analysis is well-structured and coherent.
5. Use specific musical terminology where appropriate.
6. Provide references to specific bars or notes to support your points.

Submit your analysis as a plain text string."""
        else:
            raise ValueError("Invalid task format.")

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "parameters" in t:
            validation_criteria = [
                "The composition should adhere to the given key and time signature.",
                "The composition should be exactly 8 bars in length.",
                "The format should be musical notes separated by spaces and bars by '|'."
            ]
        else:
            validation_criteria = [
                "The analysis should correctly identify the key and time signature.",
                "The analysis should describe the harmonic progression accurately.",
                "The analysis should provide a thoughtful interpretation of the emotional impact of the piece.",
                "The analysis should be well-structured and coherent.",
                "The analysis should use specific musical terminology where appropriate.",
                "The analysis should reference specific bars or notes to support the points made."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
