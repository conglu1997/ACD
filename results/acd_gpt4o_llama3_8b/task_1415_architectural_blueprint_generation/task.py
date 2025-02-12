class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "requirements": "Design a 2-bedroom apartment with an open kitchen, one bathroom, and a small balcony. Ensure the design is functional and aesthetically pleasing.",
                "task_type": "generation"
            },
            "2": {
                "blueprint": "Living Room: 200 sq ft, Kitchen: 100 sq ft, Bedroom 1: 150 sq ft, Bedroom 2: 150 sq ft, Bathroom: 50 sq ft, Balcony: 50 sq ft. Rooms are connected in a linear arrangement starting from the entrance: Living Room, Kitchen, Bedroom 1, Bathroom, Bedroom 2, Balcony.",
                "task_type": "interpretation"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'generation':
            return f"""Design an architectural blueprint based on the following requirements: {t['requirements']}. Provide a detailed description of each room, including its size, layout, and any special features. Ensure the design is functional and aesthetically pleasing. Submit your response in the following format:

Room 1: [Description of Room 1]
Room 2: [Description of Room 2]
..."""
        else:
            return f"""Interpret the following architectural blueprint: {t['blueprint']}. Describe the layout, the spatial relationships between the rooms, and any unique features of the design. Submit your response in the following format:

Layout Description: [Your description of the layout]
Spatial Relationships: [Your description of the spatial relationships]
Unique Features: [Your description of any unique features]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'generation':
            validation_criteria = ["The design should meet all the given requirements.", "The design should be functional and aesthetically pleasing.", "The description should include details about each room's size, layout, and special features."]
        else:
            validation_criteria = ["The interpretation should accurately describe the layout and spatial relationships.", "The interpretation should identify any unique features of the design."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
