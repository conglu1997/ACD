import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "cipher_text": "WKLV LV D FDHVDU FLSKHU",
                "historical_period": "Ancient Rome",
                "new_period": "Renaissance"
            },
            "2": {
                "cipher_text": "GUVF VF N EBGNGVBA PVCURE",
                "historical_period": "World War II",
                "new_period": "Industrial Revolution"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""This task consists of two parts:

1. Decode the following cipher text: '{t['cipher_text']}'
   This cipher is inspired by encryption methods used during the {t['historical_period']} era.
   Provide the decrypted message and explain the decryption method you used.

2. Create a new cipher inspired by encryption methods from the {t['new_period']} era.
   Encrypt the phrase 'HISTORY REPEATS ITSELF' using your new cipher.
   Provide the encrypted message and explain your encryption method, relating it to the historical context.

Format your response as follows:

Decrypted message: [Your decrypted message]
Decryption method: [Your explanation]

New cipher text: [Your encrypted message]
Encryption method: [Your explanation]
Historical context: [Brief explanation of how your cipher relates to the given historical period]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The decrypted message should be correct and the decryption method should be accurately explained.",
            f"The new cipher should be inspired by and related to the {t['new_period']} era.",
            "The encryption method for the new cipher should be clearly explained and historically plausible.",
            "The historical context provided should be relevant and accurate."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
