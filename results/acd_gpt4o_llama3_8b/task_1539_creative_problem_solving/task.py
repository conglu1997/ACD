class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "You are stuck in an elevator with no cell phone signal. Describe creative ways to get help or get out without causing damage to the elevator.",
                "task_type": "problem_solving"
            },
            "2": {
                "problem": "You need to water your plants but your watering can is broken. Describe a creative way to water your plants using common household items you might find in a kitchen.",
                "task_type": "problem_solving"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a creative and practical solution to the following everyday problem using unconventional methods or resources. Submit your solution as a plain text string.

Problem:
{t['problem']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The solution should be creative and use unconventional methods or resources.",
            "The solution should be practical and feasible in the given scenario.",
            "The solution should be clearly explained and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
