class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"pattern": ["circle", "square", "triangle", "circle", "square", "triangle", "circle", "?"]},
            "2": {"constraints": "Create a pattern using circles, squares, and triangles that repeats every 4 shapes and includes at least one of each shape."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'pattern' in t:
            return f"""Your task is to recognize the pattern in the following sequence of shapes and determine the next shape:

Pattern: {', '.join(t['pattern'][:-1])}, ?

Provide your answer as the name of the shape that should replace the question mark."""
        else:
            return f"""Your task is to create a visual pattern using circles, squares, and triangles that repeats every 4 shapes and includes at least one of each shape. Ensure the pattern follows a logical sequence and is consistent with the given constraints.

Provide your pattern as a comma-separated list of shapes. For example: circle, square, triangle, circle."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'pattern' in t:
            criteria = ["The answer should correctly identify the next shape in the sequence."]
            expected_answer = "square"  # Based on the provided pattern
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) and submission.strip().lower() == expected_answer else 0.0
        else:
            criteria = ["The pattern should repeat every 4 shapes.", "The pattern should only use circles, squares, and triangles.", "The pattern must include at least one of each shape."]
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
