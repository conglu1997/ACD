class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Write pseudocode to find the maximum number in a list of integers."},
            "2": {"description": "Write pseudocode to sort a list of numbers in ascending order using the bubble sort algorithm."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t['description']
        return f"""Convert the following natural language description into structured pseudocode:

Description: {description}

Ensure the pseudocode is clear, logically structured, and follows standard pseudocode conventions. Use common pseudocode constructs such as loops, conditionals, and function definitions. Submit your pseudocode as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
