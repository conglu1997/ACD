class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "requirements": "Design a small eco-friendly house for a family of four. The house should include 3 bedrooms, 2 bathrooms, a kitchen, a living room, and a study. The total area should not exceed 150 square meters. Incorporate sustainable features such as solar panels, rainwater harvesting, and energy-efficient appliances.",
                "constraints": "The house should fit within a rectangular plot of 200 square meters. The design should consider natural lighting and ventilation. Ensure that the living room and kitchen are adjacent, and the master bedroom has an attached bathroom."
            },
            "2": {
                "requirements": "Design a modern office space for a tech startup. The office should include open workspaces for 20 employees, 2 meeting rooms, a break area, and a small reception area. The total area should not exceed 300 square meters. Incorporate features like flexible furniture, high-speed internet infrastructure, and ergonomic workstations.",
                "constraints": "The office should fit within a rectangular floor plan of 400 square meters. The design should consider noise reduction and collaborative workspaces. Ensure that the meeting rooms are soundproof, and the break area is centrally located."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a detailed architectural design plan based on the following requirements and constraints:

Requirements:
{t['requirements']}

Constraints:
{t['constraints']}

Your design plan should include:
1. A floor plan drawing with labeled rooms and dimensions. You can represent the floor plan using a simple grid format (e.g., letters for rooms and numbers for dimensions). For example, use a grid like this:

   A A B B
   A A B B
   C C D D
   C C D D

where 'A' could be the living room, 'B' the kitchen, etc.
2. A written description explaining the design choices and how they meet the requirements and constraints.
3. Consideration of practical aspects such as lighting, ventilation, and sustainability.

Submit your response as a plain text string for the written description and the floor plan. Ensure your response is clear, comprehensive, and logically structured."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The design must meet the specified requirements and constraints.",
            "The written description must be clear and logically structured.",
            "The floor plan should accurately represent the described layout and use a simple grid format effectively."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
