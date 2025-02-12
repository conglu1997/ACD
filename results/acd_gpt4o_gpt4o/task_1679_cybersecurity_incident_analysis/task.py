class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"incident": "A company's database was found to be leaking customer information through an unsecured API endpoint. Identify the type of attack, the vulnerabilities exploited, and suggest mitigation strategies."},
            "2": {"incident": "An employee's computer was compromised through a phishing email, leading to the installation of ransomware on the company's network. Identify the type of attack, the vulnerabilities exploited, and suggest mitigation strategies."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the following cybersecurity incident and provide a detailed report. Your report should include:

1. Type of attack
2. Vulnerabilities exploited
3. Suggested mitigation strategies

Incident: {t["incident"]}

Ensure your response is clear, detailed, and addresses all parts of the task."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The report must correctly identify the type of attack.", "The report must identify the vulnerabilities exploited.", "The report must suggest appropriate mitigation strategies."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
