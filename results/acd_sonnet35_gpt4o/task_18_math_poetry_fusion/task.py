import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'math_concept': 'prime numbers',
                'syllable_structure': [5, 7, 5],
                'example_words': ['two', 'three', 'five', 'seven', 'eleven', 'thirteen', 'seventeen', 'nineteen']
            },
            {
                'math_concept': 'Fibonacci sequence',
                'syllable_structure': [3, 5, 8],
                'example_words': ['one', 'two', 'three', 'five', 'eight', 'thirteen', 'twenty-one', 'thirty-four']
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a poem that incorporates the mathematical concept of {t['math_concept']}. Your poem must follow this syllable structure for each line: {t['syllable_structure']}.

Requirements:
1. The poem must accurately represent the mathematical concept.
2. Each line must have exactly the number of syllables specified.
3. Use at least three of these words in your poem: {', '.join(t['example_words'])}.
4. The poem should be coherent and meaningful, not just a list of numbers.

Provide your response in the following format:

Poem:
[Your poem here]

Explanation:
[Briefly explain how your poem represents the mathematical concept and meets the syllable requirements]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The poem accurately represents the concept of {t['math_concept']}.",
            f"The poem follows the syllable structure: {t['syllable_structure']}.",
            f"The poem uses at least three words from the list: {', '.join(t['example_words'])}.",
            "The poem is coherent and meaningful, not just a list of numbers.",
            "The explanation clearly describes how the poem represents the mathematical concept and meets the syllable requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
