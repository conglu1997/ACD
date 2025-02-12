class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "Convert the following textual description into a diagram:", "description": "A square with a circle inside it, touching all four sides of the square. The circle has a small dot in the center."},
            "2": {"task": "Generate a textual description for the following diagram:", "diagram": "+----+\n|    |\n| [] |\n|    |\n+----+"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "description" in t:
            return f"""Your task is to convert the following textual description into a simple diagram:

{t['description']}

Ensure that the diagram is clear, accurate, and matches the description closely. Provide your diagram in a plain text format using ASCII characters. For example, if the description was 'A square with a circle inside it', a valid diagram might be:

+----+\n|    |\n| () |\n|    |\n+----+

Another example: If the description was 'A triangle with a rectangle inside it, where the rectangle's longer side is parallel to the base of the triangle', a valid diagram might be:

   /\   \n  /[]\  \n /____\ \n"""
        else:
            return f"""Your task is to generate a textual description for the following diagram:

{t['diagram']}

Ensure that the description is clear, accurate, and captures all the elements of the diagram. Provide your description in plain text format. For example, if the diagram was: 

  /\   \n /  \  \n/____\ \n
A valid description might be: 'A triangle with a horizontal line dividing it into two sections.'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The submission should accurately match the description or diagram.", "The diagram should be clear and use appropriate ASCII characters.", "The description should be precise and capture all elements of the diagram."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
