class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "game": "tic_tac_toe",
                "state": [
                    ["X", "O", "X"],
                    [" ", "X", "O"],
                    [" ", " ", " "]
                ],
                "rules": "The game is played on a 3x3 grid. Players take turns to place their mark (X or O) in an empty cell. The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins. If all nine cells are filled and neither player has three in a row, the game is a draw."
            },
            "2": {
                "game": "connect_four",
                "state": [
                    [" ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", "X", " ", " ", " "],
                    [" ", " ", "O", "X", " ", " ", " "],
                    [" ", "X", "O", "O", " ", " ", " "],
                    [" ", "O", "X", "X", " ", " ", " "],
                    ["X", "O", "X", "O", " ", " ", " "]
                ],
                "rules": "The game is played on a 7-column, 6-row grid. Players take turns to drop a disc (X or O) from the top into any of the columns. The disc falls to the lowest available position within the column. The first player to get four of their discs in a row (horizontally, vertically, or diagonally) wins. If the grid is completely filled and neither player has four in a row, the game is a draw."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        game = t["game"]
        state = t["state"]
        rules = t["rules"]
        example_move = "For example, in Tic-Tac-Toe, you might respond with (1, 0) to place your mark in the second row and first column."
        return f"Make the best strategic move in the given {game} game state following the rules provided.\n\nGame State:\n" + "\n".join([" ".join(row) for row in state]) + "\n\nRules:\n" + rules + "\n\nSubmit your move as a tuple of coordinates (row, column). {example_move}"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        game = t["game"]
        criteria = [
            "The move must be valid according to the game rules.",
            "The move must strategically advance the player's position in the game.",
            f"In {game}, the move should not result in an immediate loss in subsequent turns.",
            f"In {game}, the move should aim to win or block the opponent's win if possible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
