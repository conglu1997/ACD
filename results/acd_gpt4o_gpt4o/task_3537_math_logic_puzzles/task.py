class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "puzzle": "A farmer has a wolf, a goat, and a cabbage. He needs to cross a river with all three, but his boat can only carry himself and one other item at a time. If left together without him, the wolf will eat the goat, and the goat will eat the cabbage. How can the farmer get all three across the river safely?"
            },
            "2": {
                "puzzle": "You have a 3-gallon jug and a 5-gallon jug, and you need to measure out exactly 4 gallons of water. Neither jug has any measurement markings on it. How can you do it?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following mathematical puzzle that requires a combination of numerical calculation and logical deduction. Provide a clear and detailed explanation of your solution.

Puzzle:\n{t['puzzle']}\n
Your response should include:
1. A step-by-step explanation of how you arrived at the solution.
2. Any relevant calculations or logical inferences made along the way.

Provide your solution in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a step-by-step explanation of how the solution was arrived at.",
            "The response should include any relevant calculations or logical inferences.",
            "The solution should be correct and logically sound."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
