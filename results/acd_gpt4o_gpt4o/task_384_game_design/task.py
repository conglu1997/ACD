class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "Space Adventure", "constraints": ["The game must be designed for children aged 8-12.", "The game should involve collecting items and avoiding obstacles.", "The game should have a clear win condition."]},
            "2": {"theme": "Mystery Puzzle", "constraints": ["The game must be designed for adults.", "The game should involve solving puzzles to uncover a mystery.", "The game should include at least three levels of increasing difficulty."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        constraints = "\n".join([f"- {constraint}" for constraint in t["constraints"]])
        instructions = f"""Your task is to create a simple game concept with the following theme: {theme}. You need to explain the core mechanics, rules, and objectives of the game. Ensure that your game design adheres to the given constraints.

Constraints:
{constraints}

Provide your game design in plain text format. Include the following sections:
1. Game Concept
2. Core Mechanics
3. Rules
4. Objectives
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The game design should adhere to the given theme.",
            "The game design should comply with all the provided constraints.",
            "The core mechanics, rules, and objectives should be clearly explained.",
            "The game concept should be creative and engaging."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
