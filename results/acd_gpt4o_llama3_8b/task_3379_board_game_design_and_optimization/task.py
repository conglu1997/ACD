class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "space exploration", "constraints": {"board_size": "8x8 grid", "player_count": "2-4", "game_duration": "30-45 minutes"}},
            "2": {"theme": "medieval kingdom", "constraints": {"board_size": "10x10 grid", "player_count": "2-6", "game_duration": "45-60 minutes"}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are tasked with designing a simple board game based on the following theme and constraints:

Theme: {t['theme']}
Constraints:
- Board Size: {t['constraints']['board_size']}
- Player Count: {t['constraints']['player_count']}
- Game Duration: {t['constraints']['game_duration']}

Your task is to first design the board game, including the rules, objectives, and any necessary components (e.g., cards, pieces). Once the game is designed, optimize it to improve player engagement and balance. Ensure that the game is fun, fair, and easy to understand. Submit your response as a plain text string in the following format:

Game Design:
1. Theme: [Your game's theme]
2. Objectives: [Objectives of the game]
3. Rules: [Detailed game rules]
4. Components: [List of game components, e.g., board, cards, pieces]

Optimization:
1. Changes made: [List of changes made to optimize the game]
2. Rationale: [Explanation of why these changes improve engagement and balance]

Example format:

Game Design:
1. Theme: Space Exploration
2. Objectives: Explore planets and collect resources
3. Rules: [Detailed rules here]
4. Components: [List of components here]

Optimization:
1. Changes made: [List of changes]
2. Rationale: [Explanation of changes]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The game design should adhere to the given constraints.", "The optimization should improve player engagement and balance."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
