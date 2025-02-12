class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "ciphertext": "Uifsf jt b tfdsfu dpef", "technique": "Caesar cipher", "key": 1
            },
            "2": {
                "ciphertext": "Gur pyrnare vf gur pbqr", "technique": "ROT13", "key": None
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Decipher the following encrypted message using the specified cryptographic technique and key.

Ciphertext: {t['ciphertext']}
Technique: {t['technique']}
Key: {t['key']}

Your response should include only the decrypted message.

Example response format:
Decrypted Message: [Your decrypted message here]

Example:
Ciphertext: Uifsf jt b tfdsfu dpef
Technique: Caesar cipher
Key: 1
Decrypted Message: There is a secret code"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should only contain the decrypted message.",
            "The decrypted message should be accurate according to the given cryptographic technique and key."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
