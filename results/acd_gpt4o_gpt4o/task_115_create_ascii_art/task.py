class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "a simple house with a door and two windows"},
            "2": {"description": "a tree with a trunk and branches"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        instructions = f"""Your task is to create a piece of ASCII art based on the following description:

Description: {description}

Ensure that your ASCII art is clear, recognizable, and adheres to the given description. Your art should demonstrate creativity and attention to detail. Provide your ASCII art in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The ASCII art should match the given description.",
            "The ASCII art should be clear and recognizable.",
            "The ASCII art should demonstrate creativity and attention to detail."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
