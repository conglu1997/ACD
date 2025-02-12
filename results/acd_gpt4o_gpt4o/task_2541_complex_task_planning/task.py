class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"goal": "Organize a successful community fundraising event.", "constraints": "Budget: $5,000; Timeline: 3 months; Resources: Local volunteers, community center, local businesses."},
            "2": {"goal": "Plan a two-week international vacation for a family of four.", "constraints": "Budget: $10,000; Destinations: At least two different countries; Interests: Cultural experiences, outdoor activities."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        goal = t["goal"]
        constraints = t["constraints"]
        instructions = f"""Your task is to create a detailed, multi-step plan to achieve the following goal:

Goal: {goal}

Constraints: {constraints}

Ensure that your plan is realistic, well-structured, and takes into account all given constraints. The plan should include specific steps, timelines, and resource allocations. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The plan should be realistic and achievable within the given constraints.",
            "The plan should include specific steps, timelines, and resource allocations.",
            "The plan should be well-structured and logically organized."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
