class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "requirements": "Create a privacy policy document for a social media platform. The document should include the following sections: 1. Data Collection, 2. Data Usage, 3. User Rights, 4. Data Protection Measures."
            },
            "2": {
                "requirements": "Draft a terms of service document for an e-commerce website. The document should cover the following sections: 1. User Responsibilities, 2. Prohibited Activities, 3. Dispute Resolution, 4. Liability Limitations."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a regulatory or legal document based on the given requirements: {t['requirements']} Ensure the document is comprehensive, clearly written, and follows standard legal formatting. Use the specified section headings and provide detailed content for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The document should include all specified sections.",
            "The content should be detailed and relevant to each section.",
            "The document should be clearly written and free of grammatical errors.",
            "The document should follow standard legal formatting."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
