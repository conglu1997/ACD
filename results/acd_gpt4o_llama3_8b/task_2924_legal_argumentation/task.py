class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "issue": "Should the government have the right to access encrypted communications for national security purposes?"
            },
            "2": {
                "issue": "Should individuals have the right to refuse vaccination based on personal beliefs?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate persuasive legal arguments for and against the following legal issue:

Issue: {t['issue']}

Your response should include:
1. A clear argument in favor of the issue, supported by legal principles, precedents, and rationale.
2. A clear argument against the issue, supported by legal principles, precedents, and rationale.

Ensure that your arguments are balanced, consider multiple perspectives, and are logically structured. Address ethical, legal, and social implications in your arguments. Submit your response as a plain text string in the following format:

For the issue:
[Argument in favor]

Against the issue:
[Argument against]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The argument in favor should be clear and supported by legal principles and precedents.",
            "The argument against should be clear and supported by legal principles and precedents.",
            "The arguments should be balanced and consider multiple perspectives.",
            "The response should be logically structured and address ethical, legal, and social implications.",
            "The response should be coherent and persuasive."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
