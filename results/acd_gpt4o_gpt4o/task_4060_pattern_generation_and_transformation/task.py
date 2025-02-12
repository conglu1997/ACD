class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"pattern_rule": "Generate a pattern of numbers where each number is the sum of the previous two numbers, starting with 1 and 2, for a total of 10 numbers."},
            "2": {"initial_pattern": "1, 2, 3, 4, 5, 6", "transformation_rule": "Reverse the pattern and then double each number."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'pattern_rule' in t:
            return f"""Your task is to generate a pattern based on the following rule:

{t['pattern_rule']}

Ensure your pattern follows the rule exactly and provide the complete pattern in plain text format, with numbers separated by commas (e.g., 1, 2, 3, ...)."""
        else:
            return f"""Your task is to transform the following pattern according to the specified rule:

Initial Pattern: {t['initial_pattern']}
Transformation Rule: {t['transformation_rule']}

Ensure your transformed pattern follows the rule exactly and provide the complete pattern in plain text format, with numbers separated by commas (e.g., 2, 4, 6, ...)."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'pattern_rule' in t:
            criteria = ["The pattern should consist of 10 numbers.", "Each number should be the sum of the previous two numbers, starting with 1 and 2."]
        else:
            criteria = ["The pattern should be reversed.", "Each number in the reversed pattern should be doubled."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
