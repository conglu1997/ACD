class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "title": "Interpret Geometric Shape",
                "description": "A shape with four sides of equal length and four right angles."
            },
            "2": {
                "title": "Generate Geometric Shape",
                "criteria": "Create a shape with 6 sides, 3 of which are of equal length, and the other 3 sides forming two pairs of equal length."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['title'] == "Interpret Geometric Shape":
            instructions = f"""Your task is to interpret the given description of a geometric shape and provide its name.\n\nDescription: {t['description']}\n\nYour response should include:\n1. The name of the geometric shape (e.g., square, triangle, hexagon).\n2. A brief explanation of why the shape fits the given description.\n\nResponse Format:\nName: <name of the shape>\nExplanation: <brief explanation>"""
        elif t['title'] == "Generate Geometric Shape":
            instructions = f"""Your task is to generate a new geometric shape based on the provided criteria.\n\nCriteria: {t['criteria']}\n\nYour response should include:\n1. A description of the generated shape, including the lengths of all sides and the angles between them.\n2. Optionally, include a sketch or ASCII art representation of the shape.\n\nResponse Format:\nDescription: <description of the shape>\nSketch (optional): <optional ASCII art representation>"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['title'] == "Interpret Geometric Shape":
            criteria = [
                "The response should correctly name the geometric shape.",
                "The response should include a brief explanation of why the shape fits the given description."
            ]
        elif t['title'] == "Generate Geometric Shape":
            criteria = [
                "The generated shape should meet the provided criteria.",
                "The description should include the lengths of all sides and the angles between them.",
                "If a sketch or ASCII art representation is provided, it should accurately represent the described shape."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
