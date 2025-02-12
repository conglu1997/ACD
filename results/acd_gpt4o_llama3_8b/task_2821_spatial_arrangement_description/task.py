class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "Imagine a room with the following items: a bed, a desk, a chair, a bookshelf, and a window. Describe the arrangement of these items in a way that maximizes space and functionality for a student.", "criteria": "The description should be clear and logical, with attention to spatial relationships and usability. It should also consider factors like lighting, ease of movement, and accessibility."},
            "2": {"scenario": "Imagine an outdoor garden with the following elements: a fountain, a bench, a path, various flowers, and a tree. Describe the arrangement of these elements to create a peaceful and aesthetically pleasing environment.", "criteria": "The description should be clear and visually appealing, with attention to harmony and balance. It should also consider factors like accessibility, space utilization, and the visual impact of the arrangement."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Describe the spatial arrangement for the following scenario based on the given criteria:

Scenario: {t["scenario"]}

Ensure that your description is clear and coherent, paying attention to the spatial relationships and the specified criteria. Submit your response as a plain text string in the following format: 'Arrangement: [Your description]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [t["criteria"]]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
