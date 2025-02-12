import random
import string

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"mode": "encode", "linguistic_feature": "phonemes"},
            "2": {"mode": "decode", "linguistic_feature": "morphemes"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        base_instructions = """You are tasked with creating a custom cryptographic system based on linguistic features. Your system should use {feature} as the basis for encoding and decoding messages.

Background:
- Phonemes are the smallest units of sound in a language that can distinguish one word from another.
- Morphemes are the smallest meaningful units in a language.

For encoding:
1. Create a substitution cipher where each {feature} is replaced by a unique symbol or combination of symbols.
2. Ensure your system can handle common English words and simple sentences.
3. Provide a brief explanation of your encoding method.
4. Encode the following message: '{message}'

For decoding:
1. Analyze the given encoded message to identify patterns and potential {feature}.
2. Create a decoding key based on your analysis.
3. Decode the message using your key.
4. Provide a brief explanation of your decoding process.

Encoded message to decode: '{encoded_message}'

Your response should follow this format:

Cryptographic System Description:
[Your description here]

Encoding/Decoding Key:
[Your key here]

Encoded/Decoded Message:
[Your message here]

Explanation of Process:
[Your explanation here]
"""

        if t["mode"] == "encode":
            message = "The quick brown fox jumps over the lazy dog and finds a hidden treasure"
            return base_instructions.format(feature=t["linguistic_feature"], message=message, encoded_message="")
        else:
            encoded_message = "🔴⚪️🔵 🔶🔸🔷🔻 🔺🔹◻️🔘 🔶🔸🔷🔻 🔺🔹◻️🔘 🔶🔸🔷🔻 🔺🔹◻️🔘 🔴⚪️🔵 🔶🔸🔷🔻 🔺🔹◻️🔘 🔴⚪️🔵 🔶🔸🔷🔻"
            return base_instructions.format(feature=t["linguistic_feature"], message="", encoded_message=encoded_message)

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The cryptographic system is based on {t['linguistic_feature']} as specified.",
            "The encoding/decoding key is provided and is consistent with the described system.",
            "The encoded/decoded message is provided and appears to use the described system correctly.",
            "The explanation of the encoding/decoding process is clear, logical, and demonstrates understanding of the linguistic feature used.",
            "The response follows the specified format with all required sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
