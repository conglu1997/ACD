class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are a student who wants to convince the school principal to allow a new club. The club is focused on environmental conservation and aims to educate students on sustainability practices, organize clean-up drives, and promote eco-friendly initiatives.", "objective": "Convince the principal to approve the club by highlighting its benefits to the school and the community."},
            "2": {"scenario": "You are an employee who wants to persuade your manager to implement a remote work policy. Highlight the benefits of remote work for both employees and the company, including increased productivity, better work-life balance, and potential cost savings.", "objective": "Convince the manager to approve the remote work policy by emphasizing the positive outcomes for the team and the organization."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write a persuasive letter based on the following scenario and objective:

Scenario: {t['scenario']}
Objective: {t['objective']}

Ensure your letter is clear, logically structured, and uses persuasive language to achieve the objective. The letter should be between 200-300 words. Submit your letter as a plain text string in the following format:

Dear [Recipient],

[Body of the letter]

Sincerely,
[Your Name]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The letter should be clear and logically structured.",
            "The letter should use persuasive language to achieve the objective.",
            "The letter should be between 200-300 words.",
            "The letter should follow the specified format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
