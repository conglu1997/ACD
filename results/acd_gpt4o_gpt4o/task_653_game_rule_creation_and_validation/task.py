class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "Create a set of rules for a simple board game that can be played on a 5x5 grid. The game should involve two players, each starting at opposite corners of the grid. Define the objective of the game, the rules for player movement, and any special conditions or constraints.", "criteria": ["The rules should be clear and unambiguous.", "The rules should ensure that the game is playable and fair for both players.", "The objective of the game should be well-defined."]},
            "2": {"task": "Given the following set of game rules, validate whether the sequence of actions provided follows these rules. Provide a detailed explanation of your validation process.", "rules": "1. The game is played on a 4x4 grid. 2. Players take turns to move. 3. A player can move one space up, down, left, or right. 4. A player cannot move to a space already occupied by the other player. 5. The objective is to reach the opposite corner of the grid.", "actions": ["Player 1 moves up", "Player 2 moves down", "Player 1 moves right", "Player 2 moves left"], "criteria": ["The validation should be thorough and accurate.", "The explanation should be clear and detailed."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "rules" in t:
            instructions = f"""Your task is to validate whether the sequence of actions follows the given set of game rules. Here are the rules:\n\n{t['rules']}\n\nHere are the actions:\n\n{t['actions']}\n\nProvide a detailed explanation of your validation process. Ensure that your explanation is clear and thorough. Provide your response in the following format:\n\nValidation: [Your validation]"""
        else:
            instructions = f"""Your task is to create a set of rules for a simple board game that can be played on a 5x5 grid. The game should involve two players, each starting at opposite corners of the grid. Define the objective of the game, the rules for player movement, and any special conditions or constraints. Ensure that the rules are clear and unambiguous, that the game is playable and fair for both players, and that the objective of the game is well-defined. Provide your response in the following format:\n\nRules: [Your rules]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = t.get("criteria", [])
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
