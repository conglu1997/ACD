class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are a small business owner facing a sudden drop in sales. Provide a detailed plan to improve the business situation, considering factors like marketing, customer engagement, and cost management."},
            "2": {"scenario": "You are a project manager in charge of delivering a project on a tight deadline with limited resources. Outline a strategy to ensure successful and timely completion of the project, addressing resource allocation, risk management, and communication."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following scenario, provide a detailed and practical plan to address the issue:

Scenario: {t['scenario']}

Your plan should consider relevant factors, potential challenges, and actionable steps. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The plan should be practical and actionable.",
            "The response should address relevant factors and potential challenges.",
            "The plan should be detailed and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
