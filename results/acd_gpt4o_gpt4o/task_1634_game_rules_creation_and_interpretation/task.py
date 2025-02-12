class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "create a detailed set of rules for a board game where the objective is to collect the most points by moving pieces around a board and completing various challenges.", "requirements": ["The game should be for 2-4 players.", "The board should have at least 20 spaces.", "There should be at least 3 types of challenges players can encounter.", "Include rules for how players move, how points are scored, and how the game ends."]},
            "2": {"task": "interpret the following set of game rules and provide a step-by-step explanation of how a turn is played.", "rules": "Game: Treasure Hunt\nObjective: Collect the most treasure by the end of 10 rounds.\nSetup: Each player starts with 3 tokens and places them on any of the 5 starting points on the board.\nTurn: On your turn, you can move one of your tokens up to 3 spaces. If you land on a space with a treasure, you collect it. If you land on a space with another player's token, you must move back to your starting point.\nEnd of Game: After 10 rounds, the player with the most treasure wins."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'requirements' in t:
            return f"Your task is to {t['task']}\nAdditional requirements:\n" + "\n".join([f" - {req}" for req in t['requirements']])
        else:
            return f"Your task is to {t['task']}\nRules:\n{t['rules']}"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'requirements' in t:
            criteria = ["The rules should fulfill all the given requirements."]
        else:
            criteria = ["The explanation should be clear and accurately follow the given game rules."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
