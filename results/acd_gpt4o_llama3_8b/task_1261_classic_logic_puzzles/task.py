class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "puzzle": "Three friends, Alex, Blake, and Casey, are sitting in a row. Alex is not sitting at either end. Blake is sitting to the left of Casey. Who is sitting in the middle?"
            },
            "2": {
                "puzzle": "Four children (Emily, Mia, Noah, and Liam) are standing in a line. Emily is somewhere ahead of Mia but behind Noah. Liam is standing either at the front or the back of the line. Who is standing in the second position?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following logic puzzle:

Puzzle: {t['puzzle']}

Submit your solution as a plain text string in the format: 'Answer: [Your answer]'. Make sure your answer is derived from the given clues."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['puzzle'].startswith('Three friends'):
            criteria = [
                "The solution should be submitted in the format 'Answer: [Your answer]'.",
                "The solution should correctly identify who is sitting in the middle.",
                "The solution should be based on the given clues.",
                "The correct answer is 'Blake'."
            ]
        else:
            criteria = [
                "The solution should be submitted in the format 'Answer: [Your answer]'.",
                "The solution should correctly identify who is standing in the second position.",
                "The solution should be based on the given clues.",
                "The correct answer is 'Mia'."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
