class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "word puzzle", "constraints": "must include at least 10 words, each word must start with a different letter", "theme": "animals"},
            "2": {"type": "board game", "constraints": "must be playable by 2-4 players, should include a dice roll mechanism and movable pieces", "theme": "ancient civilizations"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a unique {t['type']} based on the following constraints and theme:

Constraints: {t['constraints']}
Theme: {t['theme']}

Ensure that your puzzle or game is original, adheres to the specified constraints, and clearly incorporates the given theme. Provide detailed instructions or rules for how the puzzle or game should be played.

Submit your response as a plain text string in the following format:

Puzzle/Game Description:
[Your detailed description here]

Instructions/Rules:
[Detailed instructions or rules for playing the puzzle or game]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The puzzle or game must be original.",
            "The puzzle or game must adhere to the specified constraints.",
            "The puzzle or game must clearly incorporate the given theme.",
            "The instructions or rules must be clear and detailed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
