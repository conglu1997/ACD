class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "There is a square room with a table in the center. Four chairs are placed around the table, one on each side. Additionally, there is a bookshelf against the north wall and a lamp in the southeast corner. Describe the arrangement in detail."},
            "2": {"description": "Imagine a rectangular garden with a fountain in the center. There are four flower beds, one in each corner of the garden. Additionally, there is a bench along the west side and a statue near the northeast corner. Describe the layout and relative positions of the elements in the garden."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the given textual description of a spatial arrangement and generate a detailed description of the arrangement. Ensure that your description is clear and accurately represents the spatial relationships described in the prompt.

{t["description"]}

Your response should include:
1. A clear and detailed description of the spatial arrangement.
2. Relative positions and orientations of the objects mentioned.
3. Any relevant spatial relationships between the objects.

Ensure your description is coherent and accurately represents the spatial relationships specified in the prompt. Format your response in plain text without any additional formatting."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a clear and detailed description of the spatial arrangement.",
            "The response should specify the relative positions and orientations of the objects mentioned.",
            "The response should accurately represent the spatial relationships described in the prompt."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
