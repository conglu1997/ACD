class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "requirements": "Design a floor plan for a small house with the following rooms: living room (20x15 ft), kitchen (15x10 ft), bedroom (15x15 ft), bathroom (10x5 ft)."
            },
            "2": {
                "requirements": "Design a floor plan for a small office space with the following rooms: reception area (10x10 ft), manager's office (15x10 ft), conference room (20x15 ft), restroom (10x5 ft)."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        requirements = t['requirements']
        return f"""Generate a simple architectural floor plan based on the following requirements: {requirements}. Ensure that the rooms are logically placed and that the overall design is functional. Label each room clearly. Submit your floor plan as a plain text string in the following format:
[room name]: [dimensions] at [location (x,y)]\n[room name]: [dimensions] at [location (x,y)]\n...
For example:
Living Room: 20x15 ft at (0,0)\nKitchen: 15x10 ft at (20,0)\nBedroom: 15x15 ft at (0,15)\nBathroom: 10x5 ft at (0,30)\n
Another example:
Reception Area: 10x10 ft at (0,0)\nManager's Office: 15x10 ft at (10,0)\nConference Room: 20x15 ft at (0,10)\nRestroom: 10x5 ft at (20,15)\n
Guidelines for logical and functional placement:
1. Ensure that adjacent rooms have shared walls where appropriate (e.g., the kitchen should be near the living room).
2. Consider the flow of movement between rooms, avoiding awkward layouts.
3. Make sure that all rooms fit within a coherent overall structure.
4. Avoid placing restrooms directly next to dining or kitchen areas if possible.
5. Ensure that the entrance to the structure leads to a common area or reception, rather than a private room.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The floor plan should include all the required rooms.",
            "The dimensions of each room should match the given requirements.",
            "The placement of rooms should be logical and functional as per the guidelines.",
            "The overall structure should be coherent and practical."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
