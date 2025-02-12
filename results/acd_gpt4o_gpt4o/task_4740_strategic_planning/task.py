class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are the manager of a tech startup developing a new AI product. You have a budget of $500,000 and 6 months to launch the product. Develop a strategic plan that includes hiring, marketing, and development. Predict potential challenges and outcomes."},
            "2": {"scenario": "You are a military strategist planning a defense strategy for a small country under potential threat. You have limited resources and need to allocate them wisely to protect key locations. Develop a strategic plan and predict potential outcomes."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to develop a strategic plan based on the following scenario and predict potential outcomes:

{t["scenario"]}

Your response should include:
1. A detailed strategic plan that outlines the steps and resource allocation.
2. Identification of potential challenges and risks.
3. Predictions of potential outcomes based on your strategic plan.
Format your response in plain text. Ensure your plan is logical, feasible, and well-structured."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The strategic plan should be detailed and well-structured.",
            "The identification of potential challenges should be clear and relevant.",
            "The predictions of potential outcomes should be logical and feasible.",
            "The response should be logical and feasible overall."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
