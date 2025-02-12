class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "challenge": "Decipher the following encoded message using a Caesar cipher with an unknown shift value:",
                "encoded_message": "Uifsf jt b tfdsfu dpef!"
            },
            "2": {
                "challenge": "Design a simple encryption algorithm that takes a plaintext message and a numeric key, and returns an encoded message. The algorithm should be both reversible and secure against simple frequency analysis attacks. Include an example encryption and decryption process."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""{t['challenge']}

If the task involves deciphering, provide the decoded message and explain the steps taken to reach the solution. If the task involves designing an encryption algorithm, describe the algorithm, provide an example encryption and decryption process, and explain why the algorithm is secure against simple frequency analysis attacks.

Submit your response as a plain text string with the following sections:

1. Solution: [Your solution here]
2. Explanation: [Your explanation here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "encoded_message" in t:
            criteria = ["The decoded message should be 'There is a secret code!'.", "The explanation should detail the steps taken to decipher the message, including how the shift value was determined."]
        else:
            criteria = ["The encryption algorithm should be reversible and secure against simple frequency analysis attacks.", "The example encryption and decryption process should be correct and clearly explained.", "The explanation should describe why the algorithm is secure against simple frequency analysis attacks, with specific examples."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
