class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "structure_type": "modern residential house",
                "requirements": "2 bedrooms, 1 kitchen, 1 living room, eco-friendly materials, energy-efficient design"
            },
            "2": {
                "structure_type": "urban community center",
                "requirements": "multi-purpose hall, library, outdoor playground, accessible design, sustainable architecture"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an architectural structure based on the given criteria and provide a detailed critique of the design. Ensure your design is detailed and covers all aspects, including layout, materials, and unique features. After describing the design, provide a critique evaluating how well the design meets the specified requirements and suggesting improvements.

Structure Type: {t['structure_type']}
Requirements: {t['requirements']}

Format your response as follows:
1. Design Description: [Your design description]
2. Critique: [Your critique]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The design should be detailed and cover layout, materials, and unique features.",
            "The critique should evaluate how well the design meets the specified requirements.",
            "The critique should suggest improvements.",
            "The response should be coherent and logically structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
