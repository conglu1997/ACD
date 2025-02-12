class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "ascii_art": "\n  *  \n *** \n*****\n  |  \n  |  \n",
                "transformation": "Flip horizontally"
            },
            "2": {
                "ascii_art": "\n @ \n/|\\\n | \n/ \ ",
                "transformation": "Rotate 90 degrees clockwise"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given a piece of ASCII art and a specific transformation to perform on it.\n\nASCII Art:\n{t['ascii_art']}\n\nTransformation: {t['transformation']}\n\nInstructions:\n1. Carefully analyze the given ASCII art.\n2. Apply the specified transformation to the ASCII art.\n3. Ensure that the transformed ASCII art maintains the integrity of the original visual pattern.\n4. Submit your transformed ASCII art as a plain text string in the same format as the original art.\n\nExample Response Format:\nIf given ASCII art is:\n  *  \n *** \n*****\n  |  \n  |  \n\nAnd the transformation is 'Flip horizontally', the response should be:\n  *  \n *** \n*****\n  |  \n  |  \n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The transformed ASCII art should accurately reflect the specified transformation.",
            "The visual pattern should be recognizable and maintain the integrity of the original design.",
            "The submission format should be plain text and match the expected visual output."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
