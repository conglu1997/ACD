class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"instructions": ["Start with a square.", "Place a circle inside the square, touching its bottom edge.", "Add a triangle on top of the circle, with its base touching the top of the circle.", "Draw a smaller square inside the original square, aligned to the top right corner."]},
            "2": {"instructions": ["Start with a rectangle.", "Place a smaller rectangle inside it, aligned to the top left corner.", "Add a star at the center of the smaller rectangle.", "Draw a horizontal line through the center of the larger rectangle."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the following spatial instructions and describe the resulting configuration:

Instructions:
{t['instructions']}

Provide your description in plain text format, ensuring it is clear and accurately represents the final configuration based on the instructions provided. Use a format like 'The resulting configuration has...' to start your description."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
