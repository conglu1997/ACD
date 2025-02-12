class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "There are three boxes. One contains apples, one contains oranges, and one contains a mix of both. The boxes are incorrectly labeled. You can pick one fruit from one box to determine the correct labeling. Which box do you pick from and why?"},
            "2": {"puzzle": "A man is looking at a portrait. Someone asks him, 'Whose picture are you looking at?' The man replies, 'Brothers and sisters, I have none. But that man's father is my father's son.' Whose picture is the man looking at?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following logical puzzle by reasoning through the scenario and providing a solution. Here is the puzzle:

{t["puzzle"]}

Submit your solution as a plain text string, explaining your reasoning step by step in a clear and logical manner. Ensure that your explanation is detailed enough to demonstrate your reasoning process."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The reasoning should be logical and coherent.", "The solution should correctly address the puzzle.", "The explanation should be detailed enough to demonstrate the reasoning process."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
