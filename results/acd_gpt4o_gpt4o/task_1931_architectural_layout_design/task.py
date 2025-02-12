class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"requirements": "Design a one-bedroom apartment layout including a living room, kitchen, bathroom, and bedroom. The total area should not exceed 500 square feet."},
            "2": {"requirements": "Design a small office space layout including a reception area, two private offices, a conference room, and a restroom. The total area should not exceed 800 square feet."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design an architectural layout based on the given requirements.

Requirements:
{t['requirements']}

Provide your design in the form of a detailed description, including the dimensions and placement of each room. Additionally, create a simple visual representation of the layout using text-based grid lines. Ensure that the design is practical and adheres to the specified area limit.

Format your response as follows:

Design Description:
1. [Description of the living room/office reception, including dimensions]
2. [Description of the kitchen/private office, including dimensions]
...

Visual Representation:
[Your text-based grid representation of the layout]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The design must include all specified rooms.",
            "The dimensions and layout must be practical and adhere to the area limit.",
            "The description must be clear and detailed.",
            "The visual representation must accurately reflect the described layout."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
