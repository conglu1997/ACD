class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "room_type": "Living Room",
                "requirements": "Include a seating area for 6 people, a TV, a coffee table, and a bookshelf. Ensure there is enough space for movement.",
                "constraints": "Room dimensions are 20x15 feet. The door is located in the middle of the north wall."
            },
            "2": {
                "room_type": "Home Office",
                "requirements": "Include a desk, a chair, a filing cabinet, and sufficient lighting. Ensure an ergonomic setup for long work hours.",
                "constraints": "Room dimensions are 12x10 feet. The window is located on the east wall."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create an interior design blueprint for the specified room based on the given requirements and constraints.

Room Type: {t['room_type']}

Requirements:
{t['requirements']}

Constraints:
{t['constraints']}

In your response, include the following sections:
1. Blueprint: Provide a detailed blueprint of the room layout using a simple grid system. Use the following symbols to denote elements:
    - 'D' for door
    - 'W' for window
    - 'C' for chair
    - 'T' for table
    - 'B' for bookshelf
    - 'S' for sofa
    - 'F' for filing cabinet
    - 'L' for lamp
    - 'TV' for television
    - 'X' for other items
2. Design Choices: Explain the design choices you made, including how you ensured the requirements were met and how you addressed the constraints.

Ensure that your blueprint is clear and accurately represents the room layout. The design choices should be logical and demonstrate a good understanding of interior design principles. Submit your response as a plain text string.

Example response format:

Blueprint:
D.................
..................W
..................W
.C.............L..
.TV........B...L..
.S..T......T..S...
.S.............S..

Design Choices:
- Choice 1: Placed the sofas (S) to create a comfortable seating area around the coffee table (T).
- Choice 2: Positioned the bookshelf (B) along the wall to maximize floor space.
- Choice 3: Ensured that the door (D) and windows (W) were easily accessible.
- Choice 4: Placed the TV (TV) in a central location for optimal viewing.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The blueprint should be clear and accurately represent the room layout using the specified symbols.",
            "The design choices should be logical and address the requirements and constraints.",
            "The response should demonstrate a good understanding of interior design principles.",
            "The explanation should be detailed and well-articulated."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
