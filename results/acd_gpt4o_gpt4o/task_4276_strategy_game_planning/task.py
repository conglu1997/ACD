class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are playing a simple turn-based strategy game where you control a character that can move one step in any of the four cardinal directions (north, south, east, west) per turn. The goal is to reach a treasure located at a specific position on a 5x5 grid. Obstacles are scattered on the grid, and you must plan your moves to avoid them and reach the treasure in the fewest possible moves. The character starts at position (0, 0), the treasure is at position (4, 4), and obstacles are at positions (2, 2), (3, 2), and (1, 3). Provide a step-by-step plan to reach the treasure in the fewest possible moves.", "explanation": "Explain your strategy and why it ensures reaching the treasure in the fewest possible moves. Ensure your explanation includes a discussion of alternative paths and why your chosen path is optimal."},
            "2": {"scenario": "You are playing a resource management game where you have to gather resources and build structures to achieve a specific goal. You start with 10 units of wood and 5 units of stone. Each turn, you can either gather 5 units of wood or 3 units of stone, or build a structure. A house requires 10 units of wood and 5 units of stone, and a farm requires 15 units of wood and 10 units of stone. The goal is to build 2 houses and 1 farm in the fewest number of turns. Provide a turn-by-turn plan to achieve this goal.", "explanation": "Explain your strategy and why it ensures achieving the goal in the fewest number of turns. Include a discussion on resource prioritization and turn efficiency."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to devise a strategy to achieve a specific goal within the given game scenario.

Scenario: {t['scenario']}

After devising the strategy, explain how it works and why it ensures achieving the goal in the fewest possible moves/turns. Your explanation should be clear, detailed, and include any relevant logical reasoning. Provide your response in plain text format with the following structure:

Strategy:
[Your strategy here]

Explanation:
[Your explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The strategy should correctly achieve the goal within the constraints of the scenario.",
            "The explanation should be clear and detailed.",
            "The explanation should accurately describe how the strategy works.",
            "The strategy should be optimal in terms of the number of moves/turns.",
            "The explanation should discuss alternative paths/strategies and justify the chosen one as optimal."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
