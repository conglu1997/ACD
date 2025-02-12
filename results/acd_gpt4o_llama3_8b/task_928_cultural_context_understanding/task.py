class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"reference": "In Japan, giving a sharp object as a gift is considered bad luck unless the receiver gives a coin in return."},
            "2": {"reference": "In Spain, it is customary to eat 12 grapes at midnight on New Year's Eve, one for each stroke of the clock."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret and explain the cultural reference provided below:

{t["reference"]}

Provide your explanation in a clear and concise manner as a plain text string in the following format:

Explanation: [Your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should accurately interpret the cultural reference.", "The explanation should be clear and concise."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
