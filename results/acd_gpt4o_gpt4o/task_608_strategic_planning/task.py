class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"goal": "plan a 7-day travel itinerary", "constraints": "budget of $1000, travel to 3 different cities, include at least 2 activities per city"},
            "2": {"goal": "plan a project timeline for developing a mobile app", "constraints": "complete within 3 months, involve 5 team members, include at least 5 milestones"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        goal = t["goal"]
        constraints = t["constraints"]
        instructions = f"""Your task is to plan a multi-step process to achieve the following goal:

Goal: {goal}

Constraints: {constraints}

Ensure your plan is detailed, logical, and adheres to all the given constraints. Provide your plan in plain text format, with each step clearly labeled and explained."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The plan should be detailed and logical.",
            "The plan should adhere to all given constraints.",
            "The steps should be clearly labeled and explained."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
