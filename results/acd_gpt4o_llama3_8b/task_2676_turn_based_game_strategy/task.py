class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "game_rules": "The game is played on a 3x3 grid. Players take turns placing their mark (X or O) in an empty cell. The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins. If all cells are filled without a winner, the game is a draw.",
                "instructions": "Devise a strategy for the first player (X) to maximize their chances of winning. Explain the reasoning behind your chosen moves and how they lead to a winning strategy or a draw. Your strategy should consider different possible responses from the opponent (O). Submit your strategy as a plain text string in the following format:\n\nStrategy: [Your strategy here]\nExplanation: [Your explanation here]."
            },
            "2": {
                "game_state": "X | O | \nO | X | \n |  | ",
                "instructions": "Given the current game state, devise the next move for player X that maximizes their chances of winning. Explain your reasoning and how this move fits into the overall strategy. Submit your move as a coordinate (row, column) and your explanation as a plain text string in the following format:\n\nMove: (row, column)\nExplanation: [Your explanation here]."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return t["instructions"]

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "game_rules" in t:
            validation_criteria = [
                "The strategy should maximize the chances of winning for player X.",
                "The explanation should be coherent and consider different possible responses from the opponent (O)."]
        else:
            validation_criteria = [
                "The move should be optimal given the current game state.",
                "The explanation should clearly justify why this move maximizes the chances of winning."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
