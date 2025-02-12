class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are an employee at a company and need to request a week off for a family event. Write an email to your manager explaining the reason for your leave request and ensuring it sounds professional."},
            "2": {"scenario": "You are the head of a project team and need to inform a client about a delay in the project due to unforeseen circumstances. Write an email explaining the situation, apologizing for the delay, and providing a new timeline for completion."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write a formal email based on the following scenario:

{t['scenario']}

Ensure that the email adheres to the following requirements:
1. Use a professional tone appropriate for the situation.
2. Clearly explain the reason for the email.
3. Be concise but provide all necessary details.
4. Use proper email formatting including a subject line, greeting, body, and closing.

Submit your email as a plain text string.

Example format:
Subject: Request for Leave

Dear [Recipient's Name],

I am writing to request a week off from [start date] to [end date] for a family event. I have ensured that my current tasks are up-to-date and have delegated any urgent matters to my colleagues. I would greatly appreciate your understanding and approval for this leave.

Sincerely,
[Your Name]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The email should use a professional tone appropriate for the situation.",
            "The email should clearly explain the reason for the communication.",
            "The email should be concise but provide all necessary details.",
            "The email should use proper formatting including a subject line, greeting, body, and closing."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
