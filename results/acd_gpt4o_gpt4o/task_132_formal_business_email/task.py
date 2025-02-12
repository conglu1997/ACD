class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are an employee requesting a meeting with your manager to discuss your performance review.", "email_components": {"subject": "Request for Performance Review Meeting", "greeting": "Dear [Manager's Name],", "closing": "Best regards,\n[Your Name]"}},
            "2": {"scenario": "You are a project manager updating a client on the progress of a project and outlining the next steps.", "email_components": {"subject": "Project Update and Next Steps", "greeting": "Dear [Client's Name],", "closing": "Sincerely,\n[Your Name]"}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following scenario, compose a formal business email using the provided components.

Scenario: {t['scenario']}

Ensure your email includes the following components:
- Subject: {t['email_components']['subject']}
- Greeting: {t['email_components']['greeting']}
- Closing: {t['email_components']['closing']}
- A middle paragraph that elaborates on the context and purpose of the email.

Your email should be clear, professional, and appropriate for the given context. The email should be between 150 and 250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
