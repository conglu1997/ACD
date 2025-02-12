class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "legal_text": "In the event of a breach of contract, the non-breaching party shall be entitled to seek damages equivalent to the loss incurred, provided that such loss is a direct consequence of the breach and was foreseeable at the time of contract formation."
            },
            "2": {
                "legal_text": "Any disputes arising out of or in connection with this agreement shall be resolved through binding arbitration in accordance with the rules of the American Arbitration Association, and judgment upon the award rendered by the arbitrator(s) may be entered in any court having jurisdiction thereof."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following tasks based on the provided legal text:

1. Summarize the main point of the given legal text.
2. Explain any conditions or limitations mentioned in the text.
3. Provide a practical example illustrating the application of the legal clause.
4. Discuss any potential ambiguities or areas where interpretation might vary.

Submit your response as a plain text string in the following format:

Summary:
[Your summary]

Conditions:
[Your explanation of conditions or limitations]

Example:
[Your practical example]

Ambiguities:
[Your discussion of potential ambiguities]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The summary should accurately capture the main point of the legal text.",
            "The conditions or limitations should be clearly explained.",
            "The practical example should be relevant and illustrate the application of the legal clause.",
            "The discussion of potential ambiguities should be thoughtful and highlight possible areas of varied interpretation.",
            "The submission should be well-organized and clearly written."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
