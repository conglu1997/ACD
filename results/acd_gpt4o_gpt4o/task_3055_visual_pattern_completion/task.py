class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"pattern": "###\n# #\n###", "description": "Complete the missing part of the pattern to form a symmetric design."},
            "2": {"pattern": " * \n***\n * ", "description": "Complete the pattern by adding 3 more rows such that the entire design forms a diamond shape."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to complete the following visual pattern based on the given description.

Pattern:
{t['pattern']}

Description:
{t['description']}

Instructions:
1. Analyze the given pattern and description carefully.
2. Complete the pattern according to the description.
3. Ensure that your completed pattern is symmetric and follows the given constraints.

Format your response as follows:

Completed Pattern:
[Your completed pattern]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The completed pattern must be symmetric.", "The pattern must follow the given description and constraints."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
