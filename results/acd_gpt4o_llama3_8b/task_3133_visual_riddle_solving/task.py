class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"riddle": "A farmer has to take a wolf, a goat, and a cabbage across a river in a boat. The boat can carry only the farmer and one other item. If left together, the wolf will eat the goat, and the goat will eat the cabbage. How can the farmer get all three across the river safely?"},
            "2": {"riddle": "There are three houses in a row, each painted a different color: red, blue, and green. Three people live in these houses: Alice, Bob, and Charlie. Alice lives in the blue house. Bob does not live in the red house. Who lives in which house?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following visual riddle based on the given textual description. Provide a clear and logical explanation for your solution.

Riddle: {t["riddle"]}

Submit your response in the following format:

Solution: [Your solution here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution should be logically consistent and solve the riddle as described.", "The explanation should be clear and detailed, demonstrating the reasoning process."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
