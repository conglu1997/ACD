import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "inspiration": "Ancient Egyptian hieroglyphs and Mayan script",
                "theme": "astronomical events"
            },
            "2": {
                "inspiration": "Cuneiform and Chinese oracle bone script",
                "theme": "agricultural practices"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a fictional writing system inspired by {t['inspiration']} and use it to encode a message related to {t['theme']}. Your task has three parts:

1. Script Creation:
   a) Design a set of at least 10 unique symbols or characters for your writing system.
   b) Explain the logic behind your symbol design, including any cultural or historical influences (2-3 sentences).
   c) Describe how your script represents sounds, concepts, or words (1-2 sentences).
   d) Provide an example of how a simple word or concept (e.g., 'sun' or 'water') would be written in your script.

2. Grammar and Syntax:
   a) Outline exactly 3 basic rules for how symbols combine to form words or convey meaning.
   b) Explain how your script handles verb tenses, plurals, or other grammatical features (if applicable).

3. Message Encoding:
   a) Create a short message (3-5 words) related to {t['theme']}.
   b) Encode your message using your created script.
   c) Provide a visual representation of the encoded message (using ASCII art or a clear textual description).
   d) Explain how to decipher your encoded message (2-3 sentences).

Format your response as follows:

Script Design:
[Description of your symbols and their design logic]

Script Mechanics:
[Explanation of how your script represents language]

Example Word:
[Simple word/concept and its representation in your script]

Grammar Rules:
1. [Rule 1]
2. [Rule 2]
3. [Rule 3]

Message:
[Your original message in English]

Encoded Message:
[Visual representation of your encoded message]

Deciphering Guide:
[Explanation of how to read your encoded message]

Ensure your script is unique, culturally inspired, and logically consistent. Your encoded message should be decipherable based on the information you provide."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submission includes all required sections: Script Design, Script Mechanics, Example Word, Grammar Rules, Message, Encoded Message, and Deciphering Guide.",
            f"The created script is inspired by {t['inspiration']} and the message relates to {t['theme']}.",
            "At least 10 unique symbols or characters are described for the writing system.",
            "The script design explanation includes cultural or historical influences.",
            "An example of a simple word or concept written in the created script is provided and explained.",
            "Exactly 3 grammar rules are provided and are logically consistent and clearly explained.",
            "The encoded message is visually represented and matches the stated English message.",
            "The deciphering guide provides sufficient information to potentially decode the message.",
            "The overall script creation demonstrates creativity, cultural understanding, and internal consistency."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
