class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"passage": "The new policy will benefit hardworking employees who put in extra hours, unlike those who leave on time every day."},
            "2": {"passage": "Women are often better at multitasking, while men are usually more focused on a single task."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are provided with the following passage: '{t['passage']}' Your task is to identify any biases present in the passage and suggest modifications to make it more neutral and unbiased. Biases can include stereotypes, generalizations, or unfair comparisons. Ensure your modifications retain the original meaning as much as possible while removing biased language. Submit your modified passage as a plain text string in the following format:

Original Passage:
{t['passage']}

Modified Passage:
[Your unbiased version of the passage]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The modified passage should be free of stereotypes and generalizations.",
            "The modified passage should retain the original meaning as much as possible.",
            "The language of the modified passage should be neutral and unbiased."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
