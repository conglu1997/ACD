import random
import re

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "language": "English",
                "rule": "Replace each consonant with the next consonant in the alphabet (wrapping around from 'z' to 'b')",
                "message": "The quick brown fox jumps over the lazy dog"
            },
            {
                "language": "Spanish",
                "rule": "Reverse the order of syllables in each word, keeping the original order of words",
                "message": "El viento susurra secretos antiguos"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are a linguistic cryptographer tasked with creating and solving a cipher puzzle based on the following parameters:

Language: {t['language']}
Rule: {t['rule']}
Original message: "{t['message']}"

Your task consists of two parts:

1. Encryption (30-50 words):
   Apply the given rule to encrypt the original message. Explain your process step-by-step, including any assumptions or special cases you encounter.

2. Decryption Guide (50-70 words):
   Provide a guide for decrypting messages encoded with this cipher. Include key observations, patterns, or strategies that would help in breaking the code without prior knowledge of the specific rule.

Ensure your explanations are clear and demonstrate a deep understanding of both linguistic structures and cryptographic principles."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes both an encryption process and a decryption guide",
            "The encryption correctly applies the given rule to the original message",
            "The decryption guide provides useful strategies for breaking the code",
            "The explanation demonstrates understanding of linguistic structures and cryptographic principles",
            "The response stays within the specified word limits"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
