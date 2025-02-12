class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "code": "Khoor zruog.",
                "hint": "Caesar cipher with a shift of 3."
            },
            "2": {
                "message": "Meet me at the old oak tree at midnight.",
                "method": "Create a secret code using an Atbash cipher." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "code" in t:
            return f"Decipher the given secret code.\n\nCode:\n{t['code']}\n\nHint: {t['hint']}\n\nSubmit your answer as a plain text string in the format: \nDeciphered Message: [Your answer]"
        else:
            return f"Create a secret code for the given message using the specified method.\n\nMessage:\n{t['message']}\n\nMethod: {t['method']}\n\nSubmit your answer as a plain text string in the format: \nSecret Code: [Your answer]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "code" in t:
            criteria = [
                "The deciphered message should match the original message after applying the decryption method."
            ]
        else:
            criteria = [
                "The created secret code should accurately follow the given method and correctly encode the provided message."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
