class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "mystery"
            },
            "2": {
                "theme": "technology"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a unique puzzle based on the given theme and provide a solution for the created puzzle.

Theme: {t['theme']}

Your puzzle should be original, creative, and challenging. The solution should be clear and demonstrate the reasoning process. Ensure that the puzzle is logically sound and solvable. Submit your response as a plain text string in the following format:

Puzzle: [Your puzzle]
Solution: [Your solution]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The puzzle should be original and creative.",
            "The puzzle should be challenging.",
            "The solution should be clear and demonstrate the reasoning process.",
            "The puzzle should be logically sound and solvable."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
