import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        themes = [
            {
                "theme": "Time",
                "constraint": "Must include at least one palindrome word"
            },
            {
                "theme": "Nature",
                "constraint": "Each line must start with a consecutive letter of the alphabet"
            },
            {
                "theme": "Technology",
                "constraint": "Must only use words with an even number of letters"
            }
        ]
        return {str(i+1): theme for i, theme in enumerate(random.sample(themes, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create two interconnected riddles based on the theme '{t['theme']}' that adhere to the following constraint: {t['constraint']}.

Your task has three parts:

1. Main Riddle (3-5 lines):
   - Compose a riddle that cleverly describes an object, concept, or phenomenon related to the given theme.
   - Ensure your riddle adheres to the specified linguistic constraint.
   - The riddle should be challenging but solvable with careful thought.

2. Hint Riddle (2-3 lines):
   - Create a second, shorter riddle that serves as a hint for the main riddle.
   - This hint riddle should also adhere to the same theme and linguistic constraint.
   - It should provide a subtle clue without giving away the answer to the main riddle.

3. Explanation (4-5 sentences):
   - Provide the solution to your main riddle.
   - Explain how your riddles incorporate the given theme.
   - Describe how you adhered to the linguistic constraint in both riddles.
   - Highlight any particularly clever wordplay or misdirection used in your riddles.
   - Explain how the hint riddle relates to and provides a clue for the main riddle.

Ensure your riddles are original, engaging, and demonstrate creative use of language while adhering to the theme and constraint. Your explanation should show a clear understanding of the riddle-making process and how you've met all the requirements.

Format your response as follows:

Main Riddle:
[Your main riddle here]

Hint Riddle:
[Your hint riddle here]

Explanation:
[Your explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"Both riddles should be related to the theme '{t['theme']}'",
            f"Both riddles should adhere to the constraint: {t['constraint']}",
            "The main riddle should be original, challenging, but solvable",
            "The hint riddle should provide a subtle clue for the main riddle without giving away the answer",
            "The explanation should provide the correct solution to the main riddle",
            "The explanation should clearly describe how the theme and constraint were incorporated in both riddles",
            "The explanation should demonstrate how the hint riddle relates to the main riddle",
            "The response should follow the specified format"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
