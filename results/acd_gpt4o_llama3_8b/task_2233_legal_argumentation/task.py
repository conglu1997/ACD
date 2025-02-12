class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A company is being sued by an employee for wrongful termination. The employee claims they were fired for whistleblowing illegal activities within the company. The company argues that the employee was terminated for poor performance and insubordination."},
            "2": {"scenario": "A homeowner is suing a contractor for breach of contract. The homeowner claims that the contractor failed to complete renovations on time and did substandard work. The contractor argues that delays were due to unforeseen circumstances and that the work quality was within the industry standards."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following legal scenario, draft arguments for both the plaintiff and the defendant. Ensure each argument is logically structured, legally sound, and addresses the key points of the case. Provide clear and concise arguments for both sides.

Legal Scenario:
{t['scenario']}

Submit your arguments as a plain text string in the following format:

Plaintiff's Argument: [Your argument for the plaintiff]

Defendant's Argument: [Your argument for the defendant]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The arguments should be logically structured and legally sound.",
            "The arguments should address the key points of the case.",
            "Both sides of the argument should be clear and concise."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
