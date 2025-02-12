class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "game_genre": "Platformer",
                "criteria": [
                    "The level should include a main character, obstacles, and a goal.",
                    "There should be at least three different types of obstacles.",
                    "The goal should be to reach the end of the level without losing all lives.",
                    "Include a brief description of the setting."]
            },
            "2": {
                "game_genre": "Puzzle",
                "criteria": [
                    "The level should include a main character, puzzles, and a goal.",
                    "There should be at least three different types of puzzles.",
                    "The goal should be to solve all puzzles to unlock the next level.",
                    "Include a brief description of the setting."]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are tasked with designing a simple video game level or scenario based on the given criteria.

Game Genre: {t['game_genre']}
Criteria: {', '.join(t['criteria'])}

Submit your design as a plain text string in the following format:
1. Setting: [Brief description of the setting]
2. Main Character: [Description of the main character]
3. Obstacles/Puzzles: [Description of the obstacles or puzzles]
4. Goal: [Description of the goal]

Ensure that your design is coherent, engaging, and follows the given criteria."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The design should follow the given criteria.",
            "The setting should be briefly but clearly described.",
            "The main character should be well-defined.",
            "The obstacles in the Platformer task should be engaging and varied.",
            "The puzzles in the Puzzle task should be engaging and varied.",
            "The goal should be clear and achievable within the context of the level."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
