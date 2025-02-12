class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"game_rules": "You are playing a game called 'Island Survival'. The objective is to be the last player remaining. Each player starts on their own island with 3 resources: food, wood, and stone. Players can perform one action per turn: gather resources, build defenses, or attack another player. Gathering resources increases resources by 1, building defenses decreases the damage from attacks by 1, and attacking decreases an opponent's resources by 2. The game ends when only one player has resources remaining. Design a strategy to maximize your chances of winning.", "objective": "Be the last player remaining."},
            "2": {"game_rules": "You are playing a game called 'Treasure Hunt'. The objective is to find the hidden treasure. The game board is a 5x5 grid with each cell either being empty or containing a hint. Players can move one cell per turn in any direction (up, down, left, right). If a player lands on a hint cell, they receive a clue about the treasure's location. Design a strategy to find the treasure in the fewest number of moves.", "objective": "Find the hidden treasure in the fewest moves."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design a strategy for winning the game based on the following rules and objectives:\n\n{t["game_rules"]}\n\nObjective: {t["objective"]}\n\nProvide your strategy in plain text format, along with a brief explanation of your reasoning. Format your response as follows:\n\nStrategy: [Your strategy]\nExplanation: [Your detailed explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should clearly outline a plausible strategy for winning the game.",
            "The response should provide a detailed explanation of the reasoning behind the strategy.",
            "The strategy should be logically sound and feasible based on the game rules."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
