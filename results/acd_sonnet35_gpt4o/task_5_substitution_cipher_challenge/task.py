import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        themes = {
            'animals': ['dog', 'cat', 'fish', 'bird', 'lion', 'tiger', 'bear', 'wolf', 'fox', 'deer'],
            'colors': ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'brown', 'gray', 'black'],
            'fruits': ['apple', 'banana', 'orange', 'grape', 'mango', 'peach', 'pear', 'cherry', 'kiwi', 'lemon'],
            'countries': ['usa', 'china', 'india', 'brazil', 'russia', 'japan', 'france', 'italy', 'spain', 'canada']
        }
        theme = random.choice(list(themes.keys()))
        return {
            "1": {"theme": theme, "words": themes[theme], "mode": "encode"},
            "2": {"theme": theme, "words": themes[theme], "mode": "decode"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['mode'] == 'encode':
            return f"""Create a simple substitution cipher based on the theme '{t['theme']}'.
            1. Use the following words for your cipher: {', '.join(t['words'])}.
            2. Assign each letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' to one of these words. You may use each word multiple times.
            3. Using your cipher, encode the message: 'THE QUICK BROWN FOX'
            4. Provide your response in the following format:
               Cipher key: A:word1, B:word2, C:word3, ..., Z:word10
               Encoded message: word word word word"""
        else:
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            cipher = {letter: random.choice(t['words']) for letter in alphabet}
            message = 'THE QUICK BROWN FOX'
            encoded_message = ' '.join([cipher.get(c, c) for c in message if c != ' '])
            return f"""Decode the following message that has been encoded using a substitution cipher based on the theme '{t['theme']}'.
            The encoded message is: {encoded_message}
            Each word in the encoded message represents a letter in the original message.
            The cipher uses the following words: {', '.join(t['words'])}.
            Provide your response in the following format:
            Decoded message: YOUR DECODED MESSAGE HERE
            Explanation: YOUR REASONING HERE"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['mode'] == 'encode':
            criteria = [
                f"The cipher key uses words from the provided list related to the theme '{t['theme']}'.",
                "The cipher key includes assignments for all 26 letters of the alphabet.",
                "The encoded message correctly uses the provided cipher key.",
                "The response format is correct."
            ]
        else:
            criteria = [
                "The decoded message is a reasonable attempt at decoding 'THE QUICK BROWN FOX'.",
                "The explanation demonstrates understanding of the substitution cipher concept.",
                "The response format is correct."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
