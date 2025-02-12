class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "encrypt", "cipher": "Caesar", "message": "HELLO WORLD", "shift": 3},
            "2": {"task_type": "decrypt", "cipher": "Vigenère", "message": "RIJVS UYVJN", "key": "KEY"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'encrypt':
            return f"Your task is to encrypt the following message using the {t['cipher']} cipher. Apply the specified shift for the Caesar cipher.\n\nMessage: {t['message']}\nShift: {t.get('shift', '')}\n\nEncrypt the message and provide the encrypted text in plain text format.\n\nExample: If the message is 'HELLO' and the shift is 3, the encrypted message should be 'KHOOR'."
        else:
            return f"Your task is to decrypt the following message using the {t['cipher']} cipher. Use the provided key for the Vigenère cipher.\n\nMessage: {t['message']}\nKey: {t.get('key', '')}\n\nDecrypt the message and provide the decrypted text in plain text format.\n\nExample: If the message is 'RIJVS' and the key is 'KEY', the decrypted message should be 'HELLO'."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should correctly encrypt or decrypt the message based on the specified cipher and parameters.",
            "The response should be provided in plain text format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
