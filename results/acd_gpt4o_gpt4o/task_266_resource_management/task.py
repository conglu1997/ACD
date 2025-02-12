class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"goal": "Provide shelter for 100 people using limited materials.", "resources": {"wood": 500, "steel": 300, "fabric": 200}, "constraints": "The shelters must be weatherproof and provide privacy for each individual."},
            "2": {"goal": "Distribute food supplies to 5 remote villages within 3 days.", "resources": {"vehicles": 3, "drivers": 2, "food_packages": 500, "fuel_liters": 200}, "constraints": "Each village is at least 50 km apart, and roads are in poor condition."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to efficiently manage resources to achieve the following goal:

Goal: {t['goal']}

Resources available:
{t['resources']}

Constraints:
{t['constraints']}

Provide a step-by-step plan detailing how you will use the available resources to achieve the goal. Ensure that your plan is practical, feasible, and adheres to the given constraints. Provide your plan in plain text format. Your plan should include:
1. A breakdown of how each resource will be utilized.
2. A timeline for achieving the goal.
3. Consideration of any potential challenges and how to address them.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The plan should be practical and feasible.",
            "The plan should efficiently use the available resources.",
            "The plan should adhere to the given constraints.",
            "The plan should achieve the specified goal.",
            "The plan should include a breakdown of how each resource will be utilized.",
            "The plan should include a timeline for achieving the goal.",
            "The plan should consider potential challenges and how to address them."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
