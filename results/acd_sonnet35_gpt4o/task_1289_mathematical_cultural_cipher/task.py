import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {
                'culture': 'Ancient Egypt',
                'mathematical_concept': 'prime numbers',
                'message': 'The Nile floods bring life',
                'mode': 'encode'
            },
            '2': {
                'culture': 'Ancient Greece',
                'mathematical_concept': 'Fibonacci sequence',
                'message': '13 21 34 55 89 144 233',
                'mode': 'decode'
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a fictional writing system based on the culture of {t['culture']} and the mathematical concept of {t['mathematical_concept']}. Your task is to {t['mode']} the following message using this system:

{t['message']}

Your response should include the following sections, clearly labeled:

1. Writing System Description (100-150 words):
   Explain how your fictional writing system incorporates elements from {t['culture']} and the concept of {t['mathematical_concept']}. Include at least two specific cultural references and one mathematical property in your description.

2. Encoding/Decoding Rules (100-150 words):
   Provide clear, step-by-step rules for encoding and decoding messages using your system. Ensure these rules are logically consistent and incorporate both cultural and mathematical elements.

3. {t['mode'].capitalize()}d Message:
   Present the {t['mode']}d version of the given message using your system. If encoding, use a combination of symbols, numbers, or letters to represent your cipher. If decoding, provide the deciphered text in plain language.

4. Process Explanation (100-150 words):
   Offer a detailed, step-by-step explanation of how you {t['mode']}d the message using your system's rules. Include at least one mathematical calculation in your explanation.

5. Unique Feature (50-75 words):
   Describe one interesting feature or challenge of your writing system that makes it unique or difficult to decipher. Explain how this feature relates to either the cultural or mathematical aspect of your system.

Example (for reference only - do not use this exact system in your response):
- Culture: Ancient Maya
- Mathematical concept: Base-20 number system
- Encoded message: 🌽🦅3️⃣🌙2️⃣0️⃣🐍
- Decoded message: "Kukulkan returns at the solstice"

Be creative and original while ensuring your system is logically consistent and incorporates both cultural and mathematical elements. Your total response should be between 450-550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all five required sections with clear labels.",
            "The writing system description incorporates at least two specific cultural references and one mathematical property.",
            "The encoding/decoding rules are logically consistent, well-explained, and incorporate both cultural and mathematical elements.",
            "The encoded/decoded message is provided and matches the system's rules.",
            "The process explanation includes at least one mathematical calculation and follows the stated rules.",
            "The unique feature is interesting, relevant to the system, and relates to either the cultural or mathematical aspect.",
            "The response demonstrates a deep understanding of both the cultural and mathematical aspects of the task.",
            "The solution is creative and original, not mimicking the provided example.",
            "The total response is between 450-550 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0