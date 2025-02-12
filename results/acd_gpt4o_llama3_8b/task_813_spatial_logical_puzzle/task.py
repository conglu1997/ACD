class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "Five friends are sitting in a row. Their names are Alice, Bob, Charlie, Diana, and Eve. Alice is not sitting at either end. Bob is sitting to the immediate right of Diana. Charlie is sitting in the middle. Who is sitting at each position?"},
            "2": {"puzzle": "Four houses are in a row. Each house is painted a different color: red, blue, green, and yellow. The red house is not at either end. The blue house is immediately to the left of the green house. The yellow house is at one end. What is the order of the houses?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        puzzle = t['puzzle']
        return f"""Solve the following spatial logical puzzle by deducing the correct arrangement or solution based on the given clues.
Submit your response as a plain text string in the format: 'Solution: [Your solution]'. Ensure that your solution is clear and follows the sequence given in the puzzle. For example, if you think Alice is at position 1, Bob at position 2, and so on, your solution should be: 'Solution: Alice, Bob, Charlie, Diana, Eve'.

Puzzle: {puzzle}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should correctly deduce the arrangement or solution based on the given clues.",
            "The solution should be in the format 'Solution: [Your solution]'."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
