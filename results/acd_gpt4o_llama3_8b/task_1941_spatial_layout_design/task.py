class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Design a layout for a small coffee shop. The shop should include seating areas, a counter, a restroom, and a small kitchen. Provide a detailed description of the layout, including the placement of each element and any special features.",
                "constraints": {
                    "size": "500 square feet",
                    "seating_capacity": "20"
                }
            },
            "2": {
                "description": "Design a layout for a two-bedroom apartment. The apartment should include a living room, kitchen, bathroom, and two bedrooms. Provide a detailed description of the layout, including the placement of each room and any special features.",
                "constraints": {
                    "size": "800 square feet"
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a detailed layout for the following space based on the given constraints. Provide a clear and coherent description of the layout, including the placement of each element and any special features.

Description: {t['description']}
Constraints: {t['constraints']}

Ensure your description is detailed and logically structured. Submit your response as a plain text string in the following format:

Layout Description:
[Your layout description here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The layout description should be detailed and logically structured.",
            "The layout should adhere to the given constraints.",
            "The placement of elements should be reasonable and practical."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
