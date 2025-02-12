class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "space exploration", "components": ["board", "dice", "cards", "tokens"], "players": "2-4", "constraints": "Incorporate resource management and exploration mechanics."},
            "2": {"theme": "medieval kingdom", "components": ["board", "cards", "tokens", "coins"], "players": "3-6", "constraints": "Include elements of strategy and diplomacy."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to invent a new board game based on the given theme, components, and constraints. Ensure that your game is engaging, the rules are clear and coherent, and the objectives are well-defined. Provide your response in the following format:

Theme: {t['theme']}
Components: {', '.join(t['components'])}
Players: {t['players']}
Constraints: {t['constraints']}

Game Name: [Your game name]
Objective: [Describe the main objective of the game]
Setup: [Describe how to set up the game]
Rules: [List the rules of the game]
End Condition: [Describe how the game ends and how a winner is determined]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The game should be engaging.",
            "The rules should be clear and coherent.",
            "The objective should be well-defined.",
            "The game should be playable with the given components.",
            "The end condition should be clear.",
            "The game should fit the given theme.",
            "The game should incorporate the specified constraints.",
            "The game should be balanced and replayable."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
