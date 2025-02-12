class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "area_size": "1 square kilometer",
                "primary_purpose": "residential",
                "constraints": ["Include at least one park", "Must have a school", "Maximum of 3-story buildings"]
            },
            "2": {
                "area_size": "2 square kilometers",
                "primary_purpose": "commercial",
                "constraints": ["Include a central plaza", "Must have accessible public transport", "Maximum of 5-story buildings"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a small urban area based on the following criteria and constraints:

Area Size: {t['area_size']}
Primary Purpose: {t['primary_purpose']}
Constraints:
{chr(10).join('- ' + constraint for constraint in t['constraints'])}

Your design should include a detailed description of the layout, amenities, traffic flow, and green spaces. Consider practical aspects and ensure the design is coherent and logical. Submit your response as a plain text string in the following format:

Design Description: [Your detailed description here]

Example response format:
Design Description: The area is divided into four main quadrants, with a park located in the north-east quadrant. The school is located centrally to be accessible to all residents. The residential buildings are all three stories high, with roads designed to minimize traffic congestion and maximize pedestrian safety. The park includes a playground and walking trails. Residential areas are grouped around the park for easy access. Main roads are designed to encircle the residential blocks with limited access roads to reduce traffic in residential areas. The design also includes bike lanes and pedestrian walkways to promote alternative transportation methods."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The design description should be detailed and coherent.",
            "The design should meet the specified area size, primary purpose, and constraints.",
            "The layout should consider practical aspects such as traffic flow and green spaces.",
            "The design should be logical and feasible.",
            "The design should include amenities relevant to the primary purpose.",
            "The design should incorporate considerations for pedestrian and vehicle traffic."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
