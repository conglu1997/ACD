import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"range_start": 100, "range_end": 999},
            "2": {"range_start": 1000, "range_end": 9999}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""This task consists of two steps:

1. Find a narcissistic number between {t['range_start']} and {t['range_end']} (inclusive). A narcissistic number is a number that is the sum of its own digits each raised to the power of the number of digits. For example, 153 is a narcissistic number because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153. There is only one narcissistic number in the given range. Double-check your calculation to ensure accuracy.

2. Create a sentence where the length of each word corresponds to the digits of the narcissistic number you found. The sentence should relate to mathematics, numbers, or a scientific concept. For example, if you found 153, your sentence could be: 'I love math because it's logical.'

Note: When counting word lengths, ignore punctuation. Contractions (e.g., 'it's') count as the full number of letters (e.g., 'it's' is 4 letters).

The narcissistic number you find will have either 3 or 4 digits.

Provide your answer in the following format:
Narcissistic number: [your number]
Sentence: [your sentence]

Ensure that your sentence is grammatically correct, meaningful, and relates to the specified topics. Use standard words and avoid abbreviations or acronyms."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The identified number is indeed the only narcissistic number within the range {t['range_start']} to {t['range_end']}.",
            "The sentence is grammatically correct and meaningful.",
            "The lengths of the words in the sentence correspond exactly to the digits of the identified narcissistic number, following the given rules for counting word lengths.",
            "The sentence relates to mathematics, numbers, or a scientific concept, using standard words without abbreviations or acronyms."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
