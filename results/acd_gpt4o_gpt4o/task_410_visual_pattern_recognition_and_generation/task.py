class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"pattern_description": "A 3x3 grid with X's in the corners and O's in the center."},
            "2": {"criteria": "Create a 4x4 grid pattern with alternating X's and O's starting with X in the top-left corner."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'pattern_description' in t:
            return f"""Your task is to interpret the following visual pattern described in text and provide a visual representation of it in plain text format.

Pattern Description: {t['pattern_description']}

Ensure the visual representation is accurate and follows the given description.

Format: Each row of the grid should be represented on a new line, with characters separated by spaces. For example, a 2x2 grid with X's in the corners would be represented as:
X O
O X
"""
        else:
            return f"""Your task is to generate a visual pattern based on the following criteria and provide it in plain text format.

Criteria: {t['criteria']}

Ensure the visual pattern meets the specified criteria and is clearly represented.

Format: Each row of the grid should be represented on a new line, with characters separated by spaces. For example, a 2x2 grid with alternating X's and O's starting with X in the top-left corner would be represented as:
X O
O X
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'pattern_description' in t:
            criteria = ["The visual representation should accurately reflect the described pattern."]
        else:
            criteria = ["The generated pattern should meet the specified criteria and be clearly represented."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
