class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'theme': 'space exploration', 'constraints': ['must include resource management', 'must be a cooperative game', 'must have a win condition based on discovery']},
            '2': {'theme': 'medieval fantasy', 'constraints': ['must be a competitive game', 'must include character progression', 'must have a win condition based on territory control']}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t['theme']
        constraints = t['constraints']
        instructions = f"""Your task is to design a game based on the following theme and constraints.

Theme: {theme}
Constraints: {', '.join(constraints)}

Provide detailed rules and mechanics for the game. Ensure that your design adheres to the given theme and constraints. Your response should include the following elements:
1. An overview of the game's objective.
2. Detailed game rules and mechanics.
3. Explanation of how the game meets the given constraints.

Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The game design should adhere to the given theme and constraints.',
            'The rules and mechanics should be clear and detailed.',
            'The game should have a well-defined objective and win condition.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
