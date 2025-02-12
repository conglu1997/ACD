import random
import string

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mathematical_concepts = [
            "Fibonacci sequence",
            "Prime numbers",
            "Golden ratio",
            "Pascal's triangle"
        ]
        musical_elements = [
            "pitch",
            "rhythm",
            "harmony",
            "timbre"
        ]
        return {
            "1": {"math_concept": random.choice(mathematical_concepts), "musical_element": random.choice(musical_elements)},
            "2": {"math_concept": random.choice(mathematical_concepts), "musical_element": random.choice(musical_elements)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a musical cipher based on the mathematical concept of {t['math_concept']} and the musical element of {t['musical_element']}. Then, use your cipher to encode and decode a message.

1. Cipher Design (200-250 words):
   a) Explain how you incorporate {t['math_concept']} into your musical cipher.
   b) Describe how {t['musical_element']} is used in your cipher to represent letters or words.
   c) Provide a brief example of how a simple word or phrase would be encoded using your cipher.

2. Encoding (100-150 words):
   a) Encode the following message using your cipher: "QUANTUM HARMONIES"
   b) Explain the step-by-step process of encoding this message.

3. Decoding (100-150 words):
   a) Provide a short encoded message using your cipher (different from the one above).
   b) Explain how someone would decode this message using your cipher system.

4. Analysis (150-200 words):
   a) Discuss the strengths and potential vulnerabilities of your musical cipher.
   b) Compare your cipher to traditional text-based ciphers in terms of complexity and security.
   c) Explain how your cipher could be made more secure or complex.

5. Applications (100-150 words):
   a) Propose two potential real-world applications for your mathematical music cipher.
   b) Discuss any challenges that might arise in implementing these applications.

Ensure your response demonstrates a deep understanding of both the mathematical concept and the musical element, as well as their creative application in cryptography. Use clear, concise language and provide detailed explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The cipher must incorporate the mathematical concept of {t['math_concept']}.",
            f"The cipher must use the musical element of {t['musical_element']}.",
            "The response must include all five required sections: Cipher Design, Encoding, Decoding, Analysis, and Applications.",
            "The cipher design must be logically consistent and demonstrate understanding of both mathematical and musical principles.",
            "The encoding and decoding examples must be consistent with the described cipher system.",
            "The analysis must provide thoughtful insights into the strengths and weaknesses of the cipher.",
            "The proposed applications must be creative and relevant to the cipher's characteristics."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
