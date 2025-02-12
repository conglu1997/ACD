class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Create a puzzle that involves finding the longest substring of unique characters in a given string. Then provide a solution to this puzzle.",
                "input": "abrkaabcdefghijjxxx"
            },
            "2": {
                "description": "Create a puzzle that involves finding the sum of all even numbers in an array. Then provide a solution to this puzzle.",
                "input": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a programming puzzle based on the following description and provide a solution to it:

Puzzle Description: {t['description']}

Input: {t['input']}

Your response should include:
1. The puzzle statement, clearly specifying the problem to be solved.
2. The solution to the puzzle, with code and an explanation of how it works.

Ensure your puzzle statement is clear, logically consistent, and challenging. Submit your response as a plain text string in the following format:
- Puzzle Statement: [Your puzzle statement]
- Solution: [Your solution]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The puzzle statement should be clear, logically consistent, and challenging.", "The solution should correctly solve the puzzle based on the given input and should include code and an explanation."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
