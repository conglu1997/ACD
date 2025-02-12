class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "project": "Organize a community fundraiser event",
                "constraints": [
                    "The event must include at least three activities.",
                    "The event should aim to raise at least $500.",
                    "The event must be completed within one day."]
            },
            "2": {
                "project": "Develop a small vegetable garden",
                "constraints": [
                    "The garden must include at least five different types of vegetables.",
                    "The garden must be ready for planting within one month.",
                    "The garden must follow sustainable gardening practices."]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are required to create a detailed procedural plan for the following project:

Project: {t['project']}

Constraints: {', '.join(t['constraints'])}

Your plan should include the following:
1. A list of steps to complete the project.
2. A brief explanation of each step.

After creating the plan, generate a narrative that follows the steps of the plan. The narrative should demonstrate how each step is executed in the context of the project.

Submit your response in the following format:

1. Procedural Plan:
[Your list of steps with brief explanations]

2. Narrative:
[Your narrative following the steps of the plan]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The procedural plan should include a logical sequence of steps that address the project and constraints.",
            "Each step in the plan should have a brief explanation that clarifies its purpose.",
            "The narrative should follow the steps of the plan in a coherent and logical manner.",
            "The narrative should demonstrate the successful execution of the project according to the plan."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
