class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "position": "8/8/8/8/4k3/8/8/4K3 w - - 0 1",
                "description": "White to move. Generate a strategic plan to checkmate the black king in the fewest possible moves."
            },
            "2": {
                "position": "r3k2r/pppq1ppp/2nbpn2/3p4/3P4/2N1PN2/PPP2PPP/R2QKB1R w KQkq - 0 1",
                "description": "White to move. Generate a strategic plan to gain a material advantage and improve the position."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a strategic plan for the following Chess position. Your plan should consider the rules of Chess and aim to achieve the described goal. Provide a detailed explanation of your strategy and anticipated moves. Ensure your explanation is logically structured and clear. Submit your plan as a plain text string in the following format:

- Move 1: [Your move]
- Move 2: [Your move]
...

Position: {t['position']}
Description: {t['description']}

Hint: Your plan should include critical moves and the reasoning behind each move. For example, a critical move could be a check that forces the opponent's king to move, or a move that captures a high-value piece. Explain why each move is important to your overall strategy."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The strategic plan should be logically sound and follow the rules of Chess.",
            "The plan should aim to achieve the described goal.",
            "The explanation should be detailed and clearly structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
