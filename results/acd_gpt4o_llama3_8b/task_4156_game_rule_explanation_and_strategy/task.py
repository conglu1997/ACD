class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "game_rules": "The game is Tic-Tac-Toe. The board is a 3x3 grid. Players take turns marking a square with their symbol (X or O). The first player to align three of their symbols horizontally, vertically, or diagonally wins. If the board is full and no player has aligned three symbols, the game is a draw.",
                "current_state": ["X", "O", "X", " ", "O", " ", " ", " ", " "]
            },
            "2": {
                "game_rules": "The game is Connect Four. The board is a 7x6 grid. Players take turns dropping their colored disc from the top into a column. The disc falls straight down, occupying the next available space within the column. The first player to form a horizontal, vertical, or diagonal line of four of their own discs wins.",
                "current_state": [
                    [" ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", "X", " ", " ", " ", " "],
                    [" ", "O", "X", " ", " ", " ", " "],
                    [" ", "X", "O", "O", " ", " ", " "]
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given the rules of a game and the current state of the game. Your tasks are:
1. Explain the rules of the game in your own words.
2. Based on the current state of the game, suggest the best next move and justify why it is the best move.

Game Rules: {t['game_rules']}

Current State: {t['current_state']}

Submit your response as a plain text string in the following format:

Explanation: [Your explanation here]
Move: [Your suggested move here (e.g., 'Place X in the center square', 'Drop disc in column 4') with justification]

Example for Tic-Tac-Toe:
Explanation: The game is Tic-Tac-Toe, where players take turns to mark a square...
Move: Place X in the center square because it blocks the opponent from winning.

Example for Connect Four:
Explanation: The game is Connect Four, where players drop discs into a column...
Move: Drop disc in column 4 because it creates a vertical line of 3 discs, setting up for a potential win.

Please follow this format strictly."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should be clear and accurate.",
            "The suggested move should be a valid move according to the game rules.",
            "The suggested move should be strategically sound and justified based on the current state of the game."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
