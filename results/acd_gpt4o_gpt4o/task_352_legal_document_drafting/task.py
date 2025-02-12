class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"document_type": "Non-Disclosure Agreement", "details": {"parties": ["ABC Corp.", "XYZ Ltd."], "purpose": "share confidential business information for a potential partnership", "duration": "2 years", "jurisdiction": "State of California"}},
            "2": {"document_type": "Employment Contract", "details": {"employee_name": "Jane Doe", "employer_name": "Tech Innovators Inc.", "position": "Software Engineer", "salary": "$120,000 per year", "start_date": "1st January 2024", "jurisdiction": "State of New York"}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Draft a {t['document_type']} based on the following details: {t['details']}. Ensure that the document is clear, legally sound, and includes all necessary clauses and sections typically found in such documents. Provide your answer in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The document should be clear, legally sound, and include all necessary clauses and sections typically found in such documents."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
