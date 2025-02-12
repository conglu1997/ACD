class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "A triangle with sides of length 3, 4, and 5."
            },
            "2": {
                "description": "A rectangle with a length of 8 units and a width of 5 units."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        instructions = f"""Your task is to describe and analyze the given geometric figure. Provide detailed information about its properties, such as side lengths, angles, area, perimeter, and any other relevant characteristics.

Geometric Figure Description:
{description}

Submit your analysis in plain text format.
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should include all relevant properties of the geometric figure.",
            "The analysis should be accurate and coherent.",
            "The response should be in plain text format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
