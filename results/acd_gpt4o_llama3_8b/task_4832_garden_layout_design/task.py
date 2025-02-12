class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "constraints": "The garden plot is a 10x10 meter square. You need to allocate space for the following plants: tomatoes (require 2x2 meters and full sun), carrots (require 1x1 meter and partial sun), lettuce (require 1x1 meter and partial sun), and beans (require 3x3 meters and full sun). Ensure that plants with full sun requirements are not shaded by taller plants."
            },
            "2": {
                "constraints": "The garden plot is a 15x15 meter square. You need to allocate space for the following plants: cucumbers (require 2x2 meters and full sun), strawberries (require 1x1 meter and partial sun), peppers (require 1x1 meter and full sun), and corn (require 3x3 meters and full sun). Ensure that plants with full sun requirements are not shaded by taller plants."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an efficient layout for the community garden based on the following constraints:

Constraints: {t['constraints']}

Your layout should:
1. Clearly allocate space for each plant type.
2. Ensure that plants requiring full sun are not shaded by taller plants.
3. Maximize the use of available space.
4. Provide a clear and logical arrangement of plants.

Submit your layout as a plain text string describing the position and arrangement of each plant type within the given garden plot dimensions. Your description should be detailed and specify the exact coordinates or relative positions of each plant type. For example, you can describe the layout using a grid or coordinate system (e.g., 'Tomatoes at (0,0) to (2,2); Carrots at (3,3) to (4,4)'). Ensure to include considerations for plant heights and sunlight needs in your layout."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The layout should clearly allocate space for each plant type.",
            "Plants requiring full sun should not be shaded by taller plants.",
            "The layout should maximize the use of available space.",
            "The arrangement of plants should be clear and logical.",
            "The layout descriptions should be detailed and specify the exact coordinates or relative positions of each plant type.",
            "The layout should consider plant heights and sunlight needs."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
