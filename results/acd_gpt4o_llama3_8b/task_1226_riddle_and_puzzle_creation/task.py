class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "Nature",
                "constraints": "The riddle should involve at least three different elements of nature and be solvable within 3-5 lines."
            },
            "2": {
                "theme": "Technology",
                "constraints": "The puzzle should involve a common technological device and require logical reasoning to solve. The puzzle should fit within 3-5 lines."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate an original riddle or puzzle based on the following theme and constraints:

Theme: {t['theme']}

Constraints: {t['constraints']}

Your response should include:
1. The riddle or puzzle itself.
2. The solution to the riddle or puzzle.

Ensure that your riddle or puzzle is original, creative, and logically coherent. Avoid using common or overly simple riddles or puzzles.

Example Response:
Riddle/Puzzle: I can be cracked, made, told, and played. What am I?
Solution: A joke.

Submit your response as a plain text string in the following format:

Riddle/Puzzle: [Your riddle or puzzle here]
Solution: [The solution here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The response must include both the riddle/puzzle and its solution.", "The riddle/puzzle should fit the given theme and constraints.", "The riddle/puzzle should be original and solvable.", "The riddle/puzzle should be creative and logically coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
