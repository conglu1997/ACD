class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"game": "Chess", "scenario": "White to move. Position: 1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3 O-O 9. h3 Bb7 10. d4 Nd7 11. Nbd2 Bf6"},
            "2": {"game": "Checkers", "scenario": "Red to move. Position: [B, B, B, B, B, -, -, B, -, -, -, -, -, W, -, -, -, -, -, -, -, -, -, -, W, -, -, -, -, -, -, -, -, -, -, -, -, -, -, -, -, W, -, W]"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the following board game scenario and provide the best move along with a detailed explanation of the strategy behind it.

Game: {t['game']}
Scenario: {t['scenario']}

Your response should include:
1. The best move in the given scenario.
2. A detailed explanation of the strategy behind the move.
3. Any additional considerations or long-term plans relevant to the strategy.

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include a valid move.", "The strategy explanation should be coherent and logical."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
