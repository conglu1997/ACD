class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "game": "Tic-Tac-Toe",
                "rules": "Players take turns placing their marks (X or O) in an empty cell of a 3x3 grid. The first player to align three of their marks horizontally, vertically, or diagonally wins the game. If all cells are filled without any player aligning three marks, the game ends in a draw. Additionally, analyze the potential impact of the opponent's skill level on your strategy."
            },
            "2": {
                "game": "Connect Four",
                "rules": "Players take turns dropping their discs into a 6x7 grid. The first player to align four of their discs horizontally, vertically, or diagonally wins the game. If all cells are filled without any player aligning four discs, the game ends in a draw. Additionally, consider the implications of different starting positions."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to develop a strategy for winning the following game based on its rules:\n\nGame: {t['game']}\n\nRules: {t['rules']}\n\nYour strategy should include the following elements:\n1. Key opening moves and their rationale.\n2. Mid-game tactics and positioning strategies.\n3. End-game strategies to secure a win or force a draw.\n4. Anticipation of common opponent moves and counter-strategies.\n5. Analysis of the potential impact of the opponent's skill level or different starting positions on your strategy.\n\nProvide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The strategy should include key opening moves and their rationale.",
            "The strategy should describe mid-game tactics and positioning strategies.",
            "The strategy should cover end-game strategies to secure a win or force a draw.",
            "The strategy should anticipate common opponent moves and provide counter-strategies.",
            "The strategy should analyze the potential impact of the opponent's skill level or different starting positions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
