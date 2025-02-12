class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"specifications": "Create a technical drawing of a simple mechanical part. The part should be a cylindrical gear with the following dimensions: diameter 50 mm, height 20 mm, 10 teeth evenly spaced around the circumference, and a central hole with a diameter of 10 mm."},
            "2": {"drawing": "A technical drawing of a simple electrical circuit is provided: \n\nPower Source (Battery) -> Switch -> Resistor -> LED\n\nInterpret the drawing and describe the function of each component and how they are connected."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'specifications' in t:
            return f"""Your task is to generate a technical drawing based on the following specifications:\n\n{t['specifications']}\n\nEnsure that the drawing is accurate, detailed, and follows standard technical drawing conventions. You can provide your drawing in plain text format as a description or using ASCII art. Example format for ASCII art:\n\n \n|-----|\n|     |\n|-----|\n\nThis represents a simple rectangle. Be as detailed as possible in your drawing. Describe the dimensions and key features of the part."""
        elif 'drawing' in t:
            return f"""Your task is to interpret the following technical drawing and provide a detailed description of each component and their connections:\n\n{t['drawing']}\n\nEnsure that your interpretation is accurate and detailed. Describe the function of each component and how they are connected. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'specifications' in t:
            criteria = ["The drawing should accurately represent the specified part.", "The drawing should follow standard technical drawing conventions.", "The drawing should be detailed and clear.", "The drawing should describe the dimensions and key features of the part."]
        else:
            criteria = ["The interpretation should accurately describe each component.", "The interpretation should clearly explain how the components are connected.", "The interpretation should describe the function of each component."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
