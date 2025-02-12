class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "piece": "Twinkle, Twinkle, Little Star",
                "instructions": "Analyze the melody, harmony, and rhythm of the given piece. Then, create a new piece of music based on the same structure but with different notes and rhythms."
            },
            "2": {
                "piece": "Happy Birthday",
                "instructions": "Analyze the melody, harmony, and rhythm of the given piece. Then, create a new piece of music based on the same structure but in a minor key."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the musical elements in the given piece and create a new piece of music based on the instructions provided.

Piece: {t['piece']}
Instructions: {t['instructions']}

Your response should include:
1. An analysis of the melody, harmony, and rhythm of the given piece.
2. A new piece of music based on the provided instructions. For the new piece, provide the melody in musical note format (e.g., C D E F G) and describe the harmony and rhythm in plain text.

Submit your response as a plain text string in the following format:
- Analysis: [Your analysis here]
- New Piece: [Your new piece here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The analysis should clearly describe the melody, harmony, and rhythm of the given piece.",
            "The new piece should follow the structure outlined in the instructions and should be musically coherent.",
            "The response should follow the specified format precisely."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
