class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": "A triangle with sides of lengths 3, 4, and 5.",
                "instructions": "Analyze and describe the properties of the given geometric shape. Include details about its type, angles, area, perimeter, and any other relevant properties. Additionally, explain any geometric relationships or theorems that apply to this shape, such as the Pythagorean theorem. Submit your response as a plain text string in the following format: \nDescription: [Your description] \nAnalysis: [Your analysis]"
            },
            "2": {
                "data": "A circle with a radius of 7 units and an inscribed equilateral triangle.",
                "instructions": "Analyze and describe the properties of the given geometric shape. Include details about its type, circumference, area, and any other relevant properties. Additionally, explain any geometric relationships or theorems that apply to this shape, such as the relationship between the circle and the inscribed triangle. Submit your response as a plain text string in the following format: \nDescription: [Your description] \nAnalysis: [Your analysis]"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and describe the properties of the given geometric shape. Include details about its type, angles (if applicable), area, perimeter/circumference, and any other relevant properties. Additionally, explain any geometric relationships or theorems that apply to this shape. Here is the description of the shape:\n\n{t['data']}\n\nSubmit your response as a plain text string in the following format:\nDescription: [Your description] \nAnalysis: [Your analysis]\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The description should accurately capture the geometric properties described.",
            "The analysis should be coherent and correct based on the properties of the shape."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
