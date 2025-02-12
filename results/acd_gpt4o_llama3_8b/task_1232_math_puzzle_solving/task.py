class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "You have a 3-gallon jug and a 5-gallon jug. How can you measure exactly 4 gallons of water using these two jugs?"},
            "2": {"puzzle": "A farmer is traveling with a wolf, a goat, and a cabbage. He comes to a river and finds a boat that can only carry him and one other item. If left alone, the wolf will eat the goat, and the goat will eat the cabbage. How can the farmer get all three items across the river safely?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following mathematical puzzle by providing a clear and logical sequence of steps to reach the solution. Ensure that your explanation is detailed enough to demonstrate the reasoning behind each step.

Puzzle: {t['puzzle']}

Submit your solution as a plain text string in a step-by-step format. Each step should be numbered and clearly describe the action taken and its result."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should provide a clear and logical sequence of steps.",
            "The solution should correctly address the constraints and requirements of the puzzle.",
            "The solution should be detailed enough to demonstrate the reasoning behind each step.",
            "Each step should be numbered and clearly describe the action taken and its result."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
