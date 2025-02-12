class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "criteria": "Design a two-story house with the following features: a living room, a kitchen, two bedrooms, two bathrooms, a garage, and a balcony. The house should have large windows to allow natural light and an open floor plan on the ground floor. Ensure that the design is practical and aesthetically pleasing."
            },
            "2": {
                "criteria": "Design a public park with the following features: a playground, a pond, walking paths, seating areas, and a variety of trees and plants. The park should be accessible and provide a relaxing environment for visitors. Ensure that the design is functional and visually appealing."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an architectural structure based on the following criteria:

Criteria: {t['criteria']}

Your design should include a detailed description of the structure, explaining its components, spatial relationships, and how it meets the given criteria. Use clear and precise language to convey your design.

Submit your response in the following format:

- Description: [Your description here]
- Criteria Explanation: [Your explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The design should include all specified features.",
            "The design should be practical and functional.",
            "The design should be aesthetically pleasing.",
            "The description should be clear and precise, explaining the spatial relationships and components of the structure.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
