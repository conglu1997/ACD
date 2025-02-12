class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "A peaceful beach scene with a palm tree, waves, a sun setting in the background, a beach umbrella, and a sandcastle."},
            "2": {"description": "A bustling cityscape with tall buildings, cars on the street, people walking on the sidewalks, a park with trees, and a fountain."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            f"Generate a detailed step-by-step guide for drawing the following scene or object:\n{t['description']}\n\n"
            "Your instructions should be clear, specific, and provide enough detail for someone to follow and create a coherent drawing. Include instructions on proportions, positioning, and any important details. Ensure the steps are logically ordered and easy to follow. Provide your response in the following format:\n"
            "1. [Step 1: Description of what to draw first]\n2. [Step 2: Description of the next element to draw]\n..."
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The instructions should be clear and specific.",
            "The instructions should provide enough detail for someone to follow and create a coherent drawing.",
            "The steps should be logically ordered and easy to follow.",
            "The response should be in the specified format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0