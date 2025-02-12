class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Convert the following textual description into musical notation: A simple melody in C major, starting with a quarter note C, followed by a quarter note D, an eighth note E, an eighth note F, and a half note G.",
                "constraints": "The musical notation should accurately reflect the rhythm and pitch of the described melody."
            },
            "2": {
                "description": "Convert the following musical notation into a textual description: \n\nC4 | D4 | E4 F4 | G4\n\n(time signature: 4/4, each note representing a quarter note).",
                "constraints": "The textual description should accurately reflect the rhythm and pitch of the musical notation."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Convert the following musical information accurately:

Description: {t['description']}

Constraints: {t['constraints']}

Ensure that your conversion accurately reflects the rhythm and pitch specified. Submit your response in plain text format.

Examples:
1. Text to Notation: 'A simple melody in C major, starting with a quarter note C, followed by a quarter note D, an eighth note E, an eighth note F, and a half note G.' \nNotated as: 'C4 | D4 | E8 F8 | G2' (time signature: 4/4).
2. Notation to Text: 'C4 | D4 | E4 F4 | G4' (time signature: 4/4, each note representing a quarter note). \nDescribed as: 'A simple melody in C major, with quarter notes C and D, followed by quarter notes E and F, and a quarter note G.'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The conversion should accurately reflect the rhythm and pitch specified in the description.",
            "The format should be clear and consistent with standard musical notation or descriptive language."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
