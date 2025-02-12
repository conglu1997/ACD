class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are given the following constraints for arranging furniture in a rectangular room that measures 10 feet by 15 feet:\n1. The bed (6 feet by 7 feet) should be placed against the longer wall.\n2. A desk (3 feet by 5 feet) should be positioned near a window on the shorter wall.\n3. A wardrobe (4 feet by 6 feet) should be placed in a corner, not blocking the window.\n4. Ensure there is at least 2 feet of walking space around each piece of furniture."},
            "2": {"scenario": "Generate a simple floor plan for a small apartment with the following requirements:\n1. The apartment should have a bedroom, a living room, a kitchen, and a bathroom.\n2. The bedroom should be at least 120 square feet.\n3. The kitchen should be adjacent to the living room.\n4. The bathroom should be accessible from both the bedroom and the living room.\n5. Provide dimensions for each room and ensure the total area does not exceed 600 square feet."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        instructions = f"""Your task is to interpret the following scenario and generate a spatial representation based on the given constraints:

{scenario}

Ensure your response is clear and follows the spatial relationships described in the scenario. Provide your response in plain text format with a detailed description or a simple diagram if necessary. If providing a diagram, describe it clearly in text."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The spatial representation should accurately reflect the constraints and relationships described in the scenario.",
            "The description should be clear and detailed, making it easy to visualize the spatial arrangement."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
