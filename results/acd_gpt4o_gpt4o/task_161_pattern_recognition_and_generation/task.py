class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Identify the next element in the following sequence: 2, 4, 8, 16, ?"},
            "2": {"description": "Generate a sequence of 5 numbers that follows a logical pattern of your choice. Provide the rule you used to create the pattern."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following pattern recognition problem. Provide your answer in the specified format:

{t['description']}

Format: [Answer]
For Task 2, also include the pattern rule you used.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The answer should be in the correct format and logically consistent with the given or generated pattern."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
