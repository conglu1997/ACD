class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"shapes": ["square", "triangle", "circle", "hexagon"], "relationships": ["adjacent", "overlapping", "nested"], "pattern": "nested"},
            "2": {"shapes": ["rectangle", "diamond", "oval", "pentagon"], "relationships": ["adjacent", "overlapping", "nested"], "pattern": "overlapping"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the geometric puzzle based on the given shapes and their relationships. Identify the pattern and describe how the shapes should be arranged to match the specified pattern.

Shapes: {', '.join(t['shapes'])}
Relationships: {', '.join(t['relationships'])}
Pattern: {t['pattern']}

Provide your solution in a detailed description of the arrangement of shapes and their relationships. Use the following format:

Shape Arrangement: [Description of how shapes are arranged]
Relationships: [Description of how shapes are related]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should correctly identify the pattern.",
            "The solution should accurately describe the arrangement of shapes.",
            "The solution should adhere to the specified relationships between shapes."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
