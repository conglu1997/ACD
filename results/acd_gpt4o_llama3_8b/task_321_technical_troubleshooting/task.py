class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A user reports that their computer is running extremely slow despite having plenty of available disk space and RAM. The user recently installed a new software update." 
            },
            "2": {
                "scenario": "An online store's website is experiencing frequent crashes during peak hours. The server logs indicate a high number of database connection errors." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Diagnose and troubleshoot the following technical issue based on the given scenario:

Scenario: {t['scenario']}

Your response should include:
1. A clear identification of the potential root cause(s) of the issue.
2. A step-by-step troubleshooting plan to confirm the root cause.
3. Recommendations for resolving the issue.
4. Preventative measures to avoid similar issues in the future.

Ensure that your response is detailed, logical, and demonstrates a deep understanding of the technical aspects involved. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should include a clear identification of the potential root cause(s).",
            "The response should provide a logical troubleshooting plan.",
            "The response should include recommendations for resolving the issue.",
            "The response should suggest preventative measures to avoid similar issues in the future."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
