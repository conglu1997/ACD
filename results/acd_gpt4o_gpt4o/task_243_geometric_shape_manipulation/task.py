class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"shape": "L-shape (composed of 3 squares)", "transformations": ["rotate 90 degrees clockwise", "translate 2 units up", "reflect over the y-axis"], "expected_output": "L-shape (mirrored)"},
            "2": {"shapes": ["hexagon", "ellipse"], "transformations": ["rotate 45 degrees", "scale by a factor of 1.5", "translate 3 units left"], "expected_output": ["hexagon", "ellipse"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'shape' in t and 'transformations' in t:
            return f"""Your task is to apply the following transformations to the given shape. Here is the shape and the transformations:
Shape: {t['shape']}
Transformations: {', '.join(t['transformations'])}
Please describe the resulting shape and the transformation process in detail. Include descriptions of the intermediate steps for each transformation."""
        elif 'shapes' in t and 'transformations' in t:
            return f"""Your task is to apply the following transformations to each of the given shapes. Here are the shapes and the transformations:
Shapes: {', '.join(t['shapes'])}
Transformations: {', '.join(t['transformations'])}
Please describe the resulting shapes and the transformation process in detail. Include descriptions of the intermediate steps for each transformation."""
        return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should correctly describe the resulting shape(s) and the transformation process in detail, including intermediate steps."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
