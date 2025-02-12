class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"game_theme": "medieval fantasy", "puzzle_type": "logic puzzle"},
            "2": {"game_theme": "sci-fi adventure", "puzzle_type": "physical puzzle"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a puzzle for a hypothetical video game based on the following details:

Game Theme: {t['game_theme']}
Puzzle Type: {t['puzzle_type']}

Your puzzle design should include the following elements:
1. A detailed description of the puzzle mechanics, explaining how the puzzle works.
2. The solution to the puzzle, detailing the steps needed to solve it.
3. The rationale behind the puzzle design, explaining how it fits within the game's theme and enhances the player experience.

Ensure that your design is coherent, meaning the puzzle mechanics logically lead to the solution, and the rationale clearly ties the puzzle to the game's theme.

Submit your puzzle design as a plain text string in the following format:

Puzzle Mechanics: [Your detailed description of the puzzle mechanics]
Solution: [The solution to the puzzle]
Rationale: [The rationale behind the puzzle design]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The puzzle design includes a detailed description of the puzzle mechanics.", "The solution to the puzzle is clearly stated.", "The rationale behind the puzzle design explains how it fits within the game's theme and enhances the player experience."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
