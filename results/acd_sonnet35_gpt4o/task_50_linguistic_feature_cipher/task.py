import random
import re

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        topics = [
            "artificial intelligence",
            "climate change",
            "space exploration",
            "quantum computing"
        ]
        return {
            "1": {"topic": random.choice(topics), "mode": "encode"},
            "2": {"topic": random.choice(topics), "mode": "decode"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        base_instructions = (
            "This task involves creating and decoding messages using a cipher based on linguistic features. "
            "The cipher works as follows:\n"
            "1. For nouns: Replace with a synonym that has one more or one fewer syllables. (e.g., 'dog' -> 'canine')\n"
            "2. For verbs: Replace with an antonym. (e.g., 'run' -> 'walk')\n"
            "3. For adjectives: Replace with a word that starts with the next letter of the alphabet. (e.g., 'big' -> 'cold')\n"
            "4. For adverbs: Remove the word entirely.\n"
            "5. For pronouns: Replace with the next pronoun in the sequence: I, you, he, she, it, we, they. (e.g., 'I' -> 'you')\n"
            "6. For other words: Keep them unchanged.\n\n"
            "Guidelines for edge cases:\n"
            "- If a word doesn't have a clear synonym/antonym, use a related word that fits the rule.\n"
            "- If you can't find a suitable replacement, keep the original word.\n"
            "- Proper nouns should be kept unchanged.\n\n"
            "Example:\n"
            "Original: The cat sleeps soundly.\n"
            "Encoded: A feline wakes.\n\n"
        )

        if t["mode"] == "encode":
            return base_instructions + (
                f"Create a short message (1-2 sentences, maximum 20 words) related to the topic of {t['topic']}. "
                "Then, encode your message using the cipher described above. "
                "Ensure that at least 50% of the words in your message are changed during encoding. "
                "Provide your original message, the encoded message, and a brief explanation of your encoding process.\n\n"
                "Format your response as follows:\n"
                "Original message: [Your message here]\n"
                "Encoded message: [Your encoded message here]\n"
                "Encoding process: [Brief explanation of your encoding choices]"
            )
        else:  # decode mode
            return base_instructions + (
                f"Decode the following message related to {t['topic']} using the cipher described above in reverse:\n"
                "[Encoded message will be provided here]\n\n"
                "Provide your decoded message and a brief explanation of your decoding process.\n\n"
                "Format your response as follows:\n"
                "Decoded message: [Your decoded message here]\n"
                "Decoding process: [Brief explanation of your decoding choices]"
            )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        
        if t["mode"] == "encode":
            original_message = re.search(r'Original message: (.+)', submission)
            encoded_message = re.search(r'Encoded message: (.+)', submission)
            if original_message and encoded_message:
                original_words = original_message.group(1).split()
                encoded_words = encoded_message.group(1).split()
                if len(original_words) != len(encoded_words):
                    return 0.0
                changed_words = sum(1 for o, e in zip(original_words, encoded_words) if o.lower() != e.lower())
                if changed_words / len(original_words) < 0.5:
                    return 0.0
        
        criteria = [
            f"The message is related to the topic of {t['topic']}.",
            "The encoding or decoding follows the cipher rules correctly for each part of speech.",
            "The explanation of the encoding/decoding process demonstrates understanding and correct application of the cipher rules.",
            "The response format matches the instructions exactly.",
            "Edge cases are handled according to the provided guidelines.",
            "For encoding: At least 50% of the words in the original message are changed in the encoded version."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
