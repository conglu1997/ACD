class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "issue": "Should the government implement a universal basic income?"
            },
            "2": {
                "issue": "Should social media platforms be held responsible for the spread of misinformation?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        issue = t['issue']
        return f"""Generate well-reasoned arguments for and against the following social issue:\n\nIssue: {issue}\n\nYour response should include:\n1. A clear argument in favor of the issue, supported by evidence and rationale.\n2. A clear argument against the issue, supported by evidence and rationale.\nEnsure that your arguments are balanced, consider multiple perspectives, and are logically structured. Address ethical, economic, and social implications in your arguments. Format your response as follows:\n\nFor the issue:\n[Argument in favor]\n\nAgainst the issue:\n[Argument against]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The argument in favor should be well-reasoned and supported by evidence.",
            "The argument against should be well-reasoned and supported by evidence.",
            "The arguments should consider multiple perspectives, including ethical, economic, and social implications.",
            "The arguments should be logically structured and coherent."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
