class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "constraints": {
                    "building_type": "residential",
                    "number_of_floors": 2,
                    "floor_area": "2000 sq ft",
                    "rooms": [
                        {"type": "bedroom", "quantity": 3},
                        {"type": "bathroom", "quantity": 2},
                        {"type": "kitchen", "quantity": 1},
                        {"type": "living room", "quantity": 1},
                        {"type": "dining room", "quantity": 1}
                    ],
                    "additional_features": ["garage", "garden"]
                }
            },
            "2": {
                "blueprint": "[Detailed architectural blueprint in text format, describing dimensions, room placements, entry points, and any additional features such as windows or staircases]"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "constraints" in t:
            constraints = t["constraints"]
            rooms_str = ', '.join([f'{room["quantity"]} {room["type"]}(s)' for room in constraints['rooms']])
            instructions = (
                f"Your task is to generate a detailed architectural plan based on the following constraints:\n"
                f"Building Type: {constraints['building_type']}\n"
                f"Number of Floors: {constraints['number_of_floors']}\n"
                f"Total Floor Area: {constraints['floor_area']}\n"
                f"Rooms: {rooms_str}\n"
                f"Additional Features: {', '.join(constraints['additional_features'])}\n"
                "\nEnsure the plan includes room dimensions, placements, and flow between spaces. Submit your plan in plain text format with clear descriptions of each floor and room layout."
            )
        else:
            blueprint = t["blueprint"]
            instructions = (
                f"Your task is to analyze the following architectural blueprint for design elements and functionality:\n"
                f"{blueprint}\n"
                "\nProvide a detailed analysis of the blueprint, including the functionality of the design, the flow between spaces, and any potential improvements. Submit your analysis in plain text format."
            )
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "constraints" in t:
            criteria = [
                "The plan should be detailed and adhere to the given constraints.",
                "The plan should include room dimensions, placements, and flow between spaces.",
                "The plan should be clear and logically structured."
            ]
        else:
            criteria = [
                "The analysis should accurately describe the design elements and functionality.",
                "The analysis should highlight potential improvements.",
                "The analysis should be clear and precise."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
