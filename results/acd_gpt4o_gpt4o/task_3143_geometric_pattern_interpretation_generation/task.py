class TaskFamily:
    import re

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task": "interpretation",
                "pattern_description": "A grid with 3 rows and 3 columns, where the first row has all cells filled, the second row has the middle cell filled, and the third row has all cells empty."
            },
            "2": {
                "task": "generation",
                "prompt": "Generate a description of a geometric pattern with a 4x4 grid, including at least one diagonal line of filled cells."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task"] == "interpretation":
            return (
                "Your task is to interpret the following description of a geometric pattern and provide a visual representation.\n"
                f"Description: {t['pattern_description']}\n"
                "Provide your response in a grid format, using 'X' for filled cells and '.' for empty cells."
            )
        elif t["task"] == "generation":
            return (
                "Your task is to generate a detailed description of a geometric pattern based on the given prompt.\n"
                f"Prompt: {t['prompt']}\n"
                "Ensure your description is clear and can be easily visualized as a grid pattern."
            )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t["task"] == "interpretation":
            criteria = [
                "The visual representation should accurately reflect the described pattern.",
                "The grid format should use 'X' for filled cells and '.' for empty cells.",
                "The response should be coherent and correctly formatted."
            ]
        elif t["task"] == "generation":
            criteria = [
                "The description should be clear and detailed.",
                "The description should be easily visualizable as a grid pattern.",
                "The pattern should include at least one diagonal line of filled cells."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
    