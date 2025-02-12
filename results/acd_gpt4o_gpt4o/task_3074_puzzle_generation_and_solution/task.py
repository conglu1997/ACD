class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "crossword", "clues": ["A four-legged pet (3 letters)", "The color of the sky on a clear day (4 letters)", "Opposite of 'yes' (2 letters)"], "answers": ["cat", "blue", "no"]},
            "2": {"type": "logic_grid", "description": "Three friends (Alice, Bob, and Carol) each have a different favorite fruit (apple, banana, cherry). Use the clues to determine who likes which fruit.", "clues": ["Alice does not like bananas.", "Bob’s favorite fruit is not cherry.", "Carol likes apples."], "solution": {"Alice": "cherry", "Bob": "apple", "Carol": "banana"}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "crossword":
            return f"""Generate a crossword puzzle with the following clues and provide the correct answers.

Clues: {', '.join(t['clues'])}

Your response should include the crossword grid and the answers in the following format:
Grid:
[Your crossword grid]
Answers:
[Your answers corresponding to each clue]"""
        elif t["type"] == "logic_grid":
            return f"""Solve the logic grid puzzle based on the given description and clues. Provide the correct solution.

Description: {t['description']}

Clues: {', '.join(t['clues'])}

Your response should include the solution in the following format:
Solution:
[Your solution indicating who likes which fruit]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "crossword":
            criteria = ["The crossword grid should correspond to the given clues.", "The answers should be correct and match the clues."]
        elif t["type"] == "logic_grid":
            criteria = ["The solution should correctly match each friend to their favorite fruit based on the clues."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
