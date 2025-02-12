class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"role": "Software Engineer", "context": "You are applying for a software engineer position at a tech company. The interviewer asks you a series of questions about your technical skills and past projects."},
            "2": {"role": "Marketing Manager", "context": "You are applying for a marketing manager position at a retail company. The interviewer asks you about your experience in marketing campaigns and how you handle team management."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to simulate a job interview for the specified role. Here is the context:

Role: {t['role']}

Context: {t['context']}

Generate both interview questions and responses for this scenario. Ensure that your responses demonstrate appropriate professional etiquette, clear communication skills, and situational appropriateness. Provide your submission in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The questions and responses should be appropriate for the specified role.", "The responses should demonstrate clear communication skills and professional etiquette.", "The responses should be situationally appropriate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
