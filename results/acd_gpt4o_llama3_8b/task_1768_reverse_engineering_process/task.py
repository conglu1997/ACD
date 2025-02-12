class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "final_product": "A beautifully decorated cake with three layers, each a different flavor, and intricate icing designs",
                "required_elements": ["List of ingredients", "Step-by-step preparation and decoration process"]
            },
            "2": {
                "final_product": "A functional wooden chair with a cushioned seat and armrests",
                "required_elements": ["List of materials", "Step-by-step construction and assembly process"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the final product described below and deduce the steps or components that led to its creation. Ensure that your response includes all the required elements. Submit your response in the following format:

Ingredients/Materials:
- [List of ingredients/materials]

Steps:
1. [Step-by-step process]

Final Product:
{t['final_product']}

Required Elements:
{'; '.join(t['required_elements'])}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response must include a complete list of ingredients or materials.",
            "The response must include a detailed step-by-step process.",
            "The process must logically lead to the described final product.",
            "The response must be clear and coherent."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
