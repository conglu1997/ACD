import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        historical_ciphers = [
            {
                "name": "Caesar Cipher",
                "period": "Ancient Rome",
                "key_feature": "Shift alphabet by a fixed number of positions"
            },
            {
                "name": "Vigenère Cipher",
                "period": "Renaissance",
                "key_feature": "Uses a keyword to shift letters variably"
            }
        ]
        return {
            "1": random.choice(historical_ciphers),
            "2": random.choice(historical_ciphers)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze, recreate, and improve upon the {t['name']} from the {t['period']} period. This cipher's key feature is: {t['key_feature']}. Complete the following tasks:

1. Historical Context (100-150 words):
   Describe the historical and cultural context in which this cipher was used. Explain its significance and any known vulnerabilities.

2. Cipher Recreation (200-250 words):
   a) Explain the mechanics of the cipher in detail.
   b) Provide an example of encoding a short message ("SECRETMESSAGE") using this cipher. Show your work step-by-step.
   c) Describe how to decode the message, again showing your work.

3. Linguistic Analysis (150-200 words):
   Analyze how this cipher interacts with the linguistic features of the language it was primarily used for (assume it's English if not specified). Discuss any strengths or weaknesses that arise from this interaction.

4. Modern Improvement (200-250 words):
   Propose an improvement to this historical cipher that would make it more secure against modern cryptanalysis techniques. Your improvement should:
   a) Maintain the core principle of the original cipher.
   b) Address at least one major vulnerability of the original.
   c) Consider computational feasibility for both encryption and decryption.

5. Comparative Analysis (100-150 words):
   Compare your improved version to a modern encryption standard (e.g., AES). Discuss the strengths and weaknesses of your improved historical cipher in this context.

Ensure your response demonstrates a deep understanding of cryptographic principles, historical context, and creative problem-solving in combining these concepts."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of the historical cipher and its context.",
            "The cipher recreation is accurate and clearly explained.",
            "The linguistic analysis shows insight into the interaction between the cipher and language features.",
            "The proposed improvement is creative, addresses vulnerabilities, and maintains the core principle of the original cipher.",
            "The comparative analysis with modern encryption standards is thoughtful and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
