class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "notation": "C4 E4 G4 C5",
                "description": "Interpret the given musical notation and provide a textual description of the melody."
            },
            "2": {
                "constraints": "Use the C major scale, include at least 4 different notes, and follow a 4/4 time signature. The composition should be at least 4 bars long.",
                "description": "Generate a new musical composition based on the given constraints. Provide the musical notation (in ABC notation) and a textual description of the melody."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'notation' in t:
            return f"""Interpret the following musical notation and provide a textual description of the melody. Your description should include the sequence of notes, their pitch, and any notable patterns or rhythms. Ensure your explanation is clear and detailed. Submit your response as a plain text string.

Musical Notation: {t['notation']}"""
        else:
            return f"""Generate a new musical composition based on the given constraints. Provide the musical notation (in ABC notation) and a textual description of the melody. Your composition should follow the specified constraints and be creative. Submit your response as a plain text string in the following format:

Musical Notation: [Your musical notation here]
Description: [Your description here]

Constraints: {t['constraints']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = []
        if 'notation' in t:
            validation_criteria.append("The description should accurately reflect the given musical notation.")
        else:
            validation_criteria.append("The composition should follow the given constraints.")
            validation_criteria.append("The description should accurately reflect the generated musical notation.")
            validation_criteria.append("The composition should be at least 4 bars long.")
            validation_criteria.append("The composition should follow a 4/4 time signature.")
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
