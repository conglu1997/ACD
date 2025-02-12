class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "generate", "prompt": "Describe an imaginary landscape where the sky is green and the water is red."},
            "2": {"type": "interpret", "description": "A vast, rolling plain covered in purple grass, with towering, jagged mountains in the distance. In the center of the plain, there's a crystal-clear blue lake surrounded by golden trees."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "generate":
            return f"""Your task is to generate a detailed description of an imaginary landscape based on the following prompt: {t["prompt"]}. Ensure that your description is vivid, imaginative, and includes specific details about the landscape. Provide your description in a paragraph."""
        else:
            return f"""Your task is to interpret the following description of a landscape and visualize it: '{t["description"]}'. Describe the visualized landscape in your own words, ensuring that you include all the elements mentioned in the description. Provide your interpretation in a paragraph."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "generate":
            criteria = ["The description should be vivid, imaginative, and include specific details about the landscape."]
        else:
            criteria = ["The interpretation should accurately visualize the landscape described, including all mentioned elements."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
