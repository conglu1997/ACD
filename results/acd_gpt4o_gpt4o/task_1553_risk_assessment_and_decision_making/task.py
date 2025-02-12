class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are a manager in a company that has recently faced a significant data breach. You have three options: (a) immediately inform the clients and risk losing their trust, (b) investigate internally and fix the issue before informing anyone, or (c) hire an external firm to handle the situation discreetly. Assess the risks and provide a detailed decision.", "expected_result": "A detailed decision with risk assessment of each option."},
            "2": {"scenario": "You are leading a team on a high-stakes project with a tight deadline. You can either (a) push the team to work overtime and risk burnout, (b) delegate some tasks to another team and risk losing control over quality, or (c) request an extension and risk displeasing the client. Assess the risks and provide a detailed decision.", "expected_result": "A detailed decision with risk assessment of each option."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Assess the risks in the following scenario and make a strategic decision based on your assessment.

Scenario: {t['scenario']}

Provide your decision in plain text format and include a detailed risk assessment of each option."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The decision should be well-reasoned and include a detailed risk assessment of each option.", "The risk assessments should cover all provided options."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
