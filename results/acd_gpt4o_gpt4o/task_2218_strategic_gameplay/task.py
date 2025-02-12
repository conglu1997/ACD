class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "game_state": "Player A has 3 cards: [5, 7, 9]; Player B has 3 cards: [2, 6, 8]; The goal is to select a card that, when combined with the opponent's card, sums to an even number. Player A's turn.",
                "rules": "1. Players take turns selecting one card from their hand to combine with an opponent's card.\n2. The goal is to create a pair of cards that sum to an even number.\n3. If a player cannot make a valid move, they must skip their turn.\n4. The player with the most pairs at the end wins."
            },
            "2": {
                "game_state": "Player X has 2 pieces at positions [1, 4]; Player Y has 2 pieces at positions [2, 3]; The goal is to move a piece to an adjacent empty position. Player X's turn.",
                "rules": "1. Players take turns moving one piece to an adjacent empty position.\n2. Pieces can only move horizontally or vertically, not diagonally.\n3. If a player cannot make a valid move, they must skip their turn.\n4. The game ends when no more moves are possible, and the player with more pieces left on the board wins."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to evaluate the given game state and determine the best possible move based on the provided rules.

Game State: {t['game_state']}
Rules: {t['rules']}

Provide a detailed explanation of your chosen move and the reasoning behind it. Ensure that your explanation is clear, logical, and follows the rules. Provide your response in plain text format, structured as follows:

1. Chosen Move: [Description of the move]
2. Reasoning: [Explanation of why this move is the best choice]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The chosen move should be valid according to the game rules.", "The reasoning should clearly explain why the move is the best choice."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
