import random
import sympy

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'group': 'Z_7*',
                'generator': 3,
                'message': 'HELLO',
                'public_key': 4
            },
            {
                'group': 'Z_11*',
                'generator': 2,
                'message': 'WORLD',
                'public_key': 7
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a cryptographic system based on the multiplicative group {t['group']} with generator {t['generator']}. Then use your system to encode and decode the message '{t['message']}'. The public key is {t['public_key']}.

Provide your response in the following format:

1. Group Analysis (100-150 words):
   a) Explain the structure of the group {t['group']}.
   b) List all elements of the group and their orders.
   c) Verify that {t['generator']} is indeed a generator of the group.

2. Cryptosystem Design (200-250 words):
   a) Design a cryptographic system using the given group and generator.
   b) Explain how to generate public and private keys.
   c) Describe the encryption and decryption processes.
   d) Discuss the security of your system, including its strengths and potential vulnerabilities.

3. Message Encoding (100-150 words):
   a) Using the given public key {t['public_key']}, encode the message '{t['message']}'.
   b) Show your work step-by-step, including any calculations.
   c) Present the final encoded message as a sequence of numbers.

4. Message Decoding (100-150 words):
   a) Determine the private key corresponding to the given public key.
   b) Decode the message you encoded in step 3.
   c) Show your work step-by-step, including any calculations.
   d) Verify that the decoded message matches the original.

5. Algebraic Analysis (150-200 words):
   a) Prove that your encryption and decryption processes are inverse operations using group theory concepts.
   b) Discuss how the properties of the chosen group contribute to the security of your cryptosystem.
   c) Propose a potential improvement to your system using a more advanced algebraic structure (e.g., elliptic curves, polynomial rings).

Ensure your response demonstrates a deep understanding of abstract algebra and its applications to cryptography. Use appropriate mathematical notation and provide clear explanations for complex concepts. Be creative in your cryptosystem design while maintaining mathematical rigor and practical applicability."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response accurately explains the structure and elements of the given group.",
            "The cryptosystem design is mathematically sound, secure, and clearly explained.",
            "The encoding process correctly uses the given public key and results in a valid ciphertext.",
            "The decoding process correctly determines the private key and recovers the original message.",
            "The algebraic analysis demonstrates a deep understanding of group theory and its application to cryptography.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
