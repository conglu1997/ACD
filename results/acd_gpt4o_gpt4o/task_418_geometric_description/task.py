class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "shape_description": "A square with a side length of 5 units inside a circle with a radius of 7 units, both centered at the same point."
            },
            "2": {
                "shape_description": "An equilateral triangle with side length of 4 units, with a smaller equilateral triangle of side length 2 units inside it, positioned such that each vertex of the smaller triangle touches the midpoint of each side of the larger triangle."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a visual description of the following geometric shape and pattern:

{t['shape_description']}

Provide your description in plain text format, ensuring that it is clear and accurate. Your description should allow someone to visualize or draw the shape and pattern based on your words alone. Format your response as follows:

Description: <your description>"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should be clear and accurate.",
            "The description should enable someone to visualize or draw the shape and pattern based on the words alone."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0