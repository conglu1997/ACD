class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"existing_rules": "1. Each player starts with 10 points.\n2. Players take turns to roll a six-sided die.\n3. If a player rolls a 6, they gain 2 points.\n4. If a player rolls a 1, they lose 1 point.\n5. The game ends when a player reaches 20 points.\n6. Players can trade points with each other once per turn.", "goal": "Balance the game so that it is fair and engaging."},
            "2": {"game_type": "board game", "criteria": ["The game should be playable by 2-4 players.", "Each game should last approximately 45 minutes.", "The game should involve strategy, luck, and player interaction.", "Provide detailed rules, including setup, gameplay, and win conditions."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "existing_rules" in t:
            return f"""Balance the following game rules to make the game fair and engaging:\n\nExisting Rules:\n{t['existing_rules']}\n\nGoal: {t['goal']}\n\nProvide your balanced game rules in plain text format, structured as follows:\n1. Setup\n2. Gameplay\n3. Win Conditions"""
        else:
            return f"""Design a new board game based on the following criteria:\n\nGame Type: {t['game_type']}\nCriteria: {', '.join(t['criteria'])}\n\nYour game rules should include setup instructions, detailed gameplay mechanics, and win conditions. Provide your rules in plain text format, structured as follows:\n1. Setup\n2. Gameplay\n3. Win Conditions"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "existing_rules" in t:
            criteria = ["The balanced rules should create a fair game where no player has an inherent advantage and the game remains engaging.", "The rules should be clear, logically structured, and detailed."]
        else:
            criteria = ["The game rules should be clear, balanced, and meet the specified criteria for gameplay.", "The rules should include setup, gameplay, and win conditions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
