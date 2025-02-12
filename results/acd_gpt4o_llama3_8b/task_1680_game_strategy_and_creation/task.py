class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "game": "chess",
                "position": "r2q1rk1/ppp2ppp/2n1pn2/2b5/2B5/2NP1N2/PPP2PPP/R1BQ1RK1 w - - 0 1",
                "task": "Analyze the given chess position and provide the best move for White. Explain the reasoning behind your choice, considering possible responses from Black."
            },
            "2": {
                "game": "custom board game",
                "criteria": "Design a new board game that involves strategy and chance. The game should be playable by 2-4 players and should include a clear set of rules, objectives, and necessary components. Provide a detailed description of the game, its rules, and how to win."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["game"] == "chess":
            return f"""Analyze the given chess position and provide the best move for White. Explain the reasoning behind your choice, considering possible responses from Black.

Position: {t['position']}"""
        else:
            return """Design a new board game that involves strategy and chance. The game should be playable by 2-4 players and should include a clear set of rules, objectives, and necessary components. Provide a detailed description of the game, its rules, and how to win.

Your response should be structured as follows:
1. Game Name: [Name of the game]
2. Objective: [Objective of the game]
3. Components: [List of components]
4. Rules: [Detailed rules of the game]
5. Winning Conditions: [How to win the game]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["game"] == "chess":
            criteria = [
                "The response should include a valid chess move.",
                "The reasoning should consider possible responses from Black.",
                "The response should demonstrate a strong understanding of chess strategy."
            ]
        else:
            criteria = [
                "The game design should include clear rules and objectives.",
                "The game should be playable by 2-4 players.",
                "The game should involve both strategy and chance.",
                "The description should be detailed and coherent.",
                "The response should follow the provided structure."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
