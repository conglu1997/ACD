class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "Three people (Alice, Bob, and Carol) are in a room. One of them is a knight who always tells the truth, one is a knave who always lies, and one is a spy who can either lie or tell the truth. They make the following statements:\nAlice: Bob is a knave.\nBob: Carol is a spy.\nCarol: Alice is a knight.\nWho is the knight, who is the knave, and who is the spy?"},
            "2": {"puzzle": "There are three boxes. One contains only apples, one contains only oranges, and one contains both apples and oranges. Each box is labeled, but all labels are incorrect. How can you determine the contents of each box by only picking one fruit from one box?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        puzzle = t["puzzle"]
        instructions = f"""Your task is to solve the following logic puzzle and provide a clear explanation of your reasoning process.

Puzzle: {puzzle}

Provide your response in the following format:

Solution: [Your solution to the puzzle]
Explanation: [Your explanation of the reasoning process you used to arrive at the solution]

Ensure that:
1. Your solution is correct.
2. Your explanation is clear, logical, and demonstrates your reasoning process."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should be correct.",
            "The explanation should be clear, logical, and demonstrate the reasoning process used to arrive at the solution."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
