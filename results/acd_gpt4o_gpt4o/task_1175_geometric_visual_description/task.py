class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "Describe the visual arrangement of the following geometric shapes: A large blue circle to the left, a small red triangle to the right, and a medium green square in between them. Use clear and precise language to describe their positions relative to each other."},
            "2": {"task": "Interpret the following visual description and list the geometric shapes involved: 'There is a yellow hexagon at the top center, directly below it is a purple rectangle, and to the left of the rectangle, slightly lower, is an orange circle.' Provide the shapes and their relative positions."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to work with geometric shapes based on the following description. Depending on the task, you may need to either generate or interpret a visual description. Here is the task:\n\n{t['task']}\n\nSubmit your solution in plain text format. Ensure your response is clear and precise in describing or interpreting the spatial arrangement of the geometric shapes."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description must be clear and precise.", "The spatial relationships between the shapes must be accurately conveyed.", "The interpretation of the visual description must correctly identify the shapes and their positions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
