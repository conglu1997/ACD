class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are a judge in a case where an employee is suing their employer for wrongful termination. The employee claims they were fired due to their gender, which would be a violation of anti-discrimination laws. The employer argues that the termination was due to repeated tardiness. Evaluate the legal arguments and provide a judgement. Consider the following factors: 1) Evidence of gender discrimination, 2) Documentation of tardiness, 3) Company policies on termination."},
            "2": {"scenario": "You are a member of an ethics committee reviewing a case where a doctor performed a life-saving surgery without the patient's explicit consent. The patient was unconscious and in critical condition, and the surgery had to be done immediately to save their life. Analyze the ethical considerations and provide your recommendation. Consider the following factors: 1) The urgency of the situation, 2) The patient's rights, 3) The doctor's duty of care."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Evaluate the following scenario and provide a well-reasoned argument. Your response should demonstrate an understanding of the legal or ethical principles involved, and it should be clear, logical, and comprehensive. Structure your response as follows: 1) Summary of the scenario, 2) Identification of key issues, 3) Analysis of each issue, 4) Final judgement or recommendation.

Scenario: {t['scenario']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should demonstrate an understanding of the legal or ethical principles involved.",
            "The response should be clear, logical, and comprehensive.",
            "The response should provide a well-founded argument based on the scenario provided.",
            "The response should follow the specified structure: Summary, Key Issues, Analysis, Final Judgement/Recommendation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
