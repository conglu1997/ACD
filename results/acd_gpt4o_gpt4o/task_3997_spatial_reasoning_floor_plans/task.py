class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "generate", "constraints": "Generate a floor plan for a two-bedroom apartment with the following requirements: a master bedroom with an attached bathroom, a guest bedroom, a common bathroom, a kitchen, a living room, and a dining area."},
            "2": {"task_type": "interpret", "floor_plan": """Floor Plan:
- Master Bedroom: 12x15 feet, attached Bathroom: 5x8 feet
- Guest Bedroom: 10x12 feet
- Common Bathroom: 5x8 feet
- Kitchen: 8x10 feet
- Living Room: 15x20 feet
- Dining Area: 10x10 feet

The master bedroom is located at the top-left corner of the plan, with the attached bathroom to its right. The guest bedroom is adjacent to the master bedroom, sharing a wall on the right. The common bathroom is located directly below the guest bedroom and shares a wall with the kitchen to its right. The kitchen is to the right of the common bathroom. The living room is at the bottom of the plan, spanning the entire width, with the dining area at the bottom-left corner."""}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'generate':
            return f"""Your task is to generate a floor plan based on the following constraints:\n\nConstraints: {t['constraints']}\n\nEnsure that the floor plan is complete, follows the given constraints, and is easy to understand. Provide your floor plan in plain text format, describing the dimensions and relative positions of each room. Your response should be structured as follows:\n\n- Room: [dimensions and position]\n..."""
        elif t['task_type'] == 'interpret':
            return f"""Your task is to interpret the following floor plan and provide a detailed description of the layout:\n\nFloor Plan:\n{t['floor_plan']}\n\nFor each room, describe its dimensions and relative position within the plan. Ensure your descriptions are clear and comprehensive, capturing all necessary details for someone to visualize the layout. Provide your descriptions in plain text format, numbered to correspond with the rooms."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'generate':
            criteria = ["The floor plan should include all specified rooms.", "The dimensions and positions of the rooms should be clear, logical, and coherent."]
        elif t['task_type'] == 'interpret':
            criteria = ["The descriptions should accurately and comprehensively detail the layout of the floor plan.", "The spatial relationships between rooms should be logical and correctly interpreted."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
