class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "a 10x10 grid floor plan with a 4x4 square living room in the bottom left (positions 7-10, 1-4), a 4x6 rectangular kitchen on the right (positions 7-10, 5-10), and a 2x4 rectangular bathroom above the kitchen (positions 5-6, 5-8)."},
            "2": {"description": "a 10x10 grid floor plan with a 3x3 square bedroom in the top left (positions 1-3, 1-3), a 3x3 square bathroom next to the bedroom (positions 1-3, 4-6), and a 3x4 rectangular kitchen below them (positions 4-6, 1-4)."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a floor plan based on the following description: '{t["description"]}'. Ensure the floor plan is clear and resembles the described layout. The floor plan should fit within a 10x10 grid. Use 'L' for living room, 'K' for kitchen, 'B' for bathroom, and 'E' for empty space. Submit your floor plan as a plain text string with each row on a new line, e.g., 'LLLL......\nLLLL......\n......KKKK\n......KKKK\n......KKKK\n......KKKK\n......KKKK\n......KKKK\nBBBBBB....\nBBBBBB....'. Here is a detailed example of a possible floor plan response:Living room (positions 7-10, 1-4):LLLL....LLLL....LLLL....LLLL....Kitchen (positions 7-10, 5-10):.....KKKK.....KKKK.....KKKK.....KKKKBathroom (positions 5-6, 5-8):.....BBB......BBB.Empty space:E represents empty space."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
