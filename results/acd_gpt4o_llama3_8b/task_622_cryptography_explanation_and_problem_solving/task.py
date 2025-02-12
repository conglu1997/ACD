class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Explain the concept of RSA encryption and solve the following problem: Given two prime numbers p = 61 and q = 53, calculate the public key (n, e) and the private key (d) for RSA encryption. Use e = 17."
            },
            "2": {
                "prompt": "Explain the concept of symmetric key encryption and solve the following problem: Given a plaintext message 'HELLO' and a key 'XMCKL', encrypt the message using the Vigenère cipher."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Provide a detailed explanation of the following cryptographic concept and solve the related problem:

{t['prompt']}

Ensure that your explanation is clear, accurate, and demonstrates a deep understanding of the cryptographic principles involved. For the problem-solving part, show all steps and calculations clearly. Submit your response as a plain text string with the following format:

1. Explanation: [Your detailed explanation here]
2. Problem Solution: [Your step-by-step solution here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should be clear and accurate.",
            "The explanation should demonstrate a deep understanding of the cryptographic principles involved.",
            "The problem-solving part should include all steps and calculations.",
            "The final answer to the problem should be correct."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
