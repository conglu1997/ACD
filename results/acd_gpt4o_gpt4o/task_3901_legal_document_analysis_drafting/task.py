class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"document_text": "This Agreement is made on the 1st day of January, 2021, between Party A and Party B. Party A agrees to deliver 100 units of Product X to Party B by the 15th day of January, 2021. Party B agrees to pay $1,000 for the Products within 30 days of delivery. If there is any dispute, the parties agree to resolve it through arbitration. This Agreement shall be governed by the laws of State Y.", "clauses_to_find": ["delivery date", "payment terms", "governing law", "dispute resolution"]},
            "2": {"draft_criteria": "Draft a non-disclosure agreement (NDA) between Company C and Contractor D. The NDA should include clauses for confidentiality, term of agreement, governing law, and dispute resolution. The term of the agreement should be for 2 years, the governing law should be State Z, and disputes should be resolved through mediation."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'document_text' in t:
            return f"""Your task is to analyze the given legal document and identify specific clauses.

Document Text:
{t['document_text']}

Instructions:
1. Identify and list the clauses for the following:
- Delivery Date
- Payment Terms
- Governing Law
- Dispute Resolution

Your response should be in the following format:
Clauses:
- Delivery Date: [Text of the Delivery Date Clause]
- Payment Terms: [Text of the Payment Terms Clause]
- Governing Law: [Text of the Governing Law Clause]
- Dispute Resolution: [Text of the Dispute Resolution Clause]"""
        elif 'draft_criteria' in t:
            return f"""Your task is to draft a new legal document based on the given criteria.

Draft Criteria:
{t['draft_criteria']}

Instructions:
1. Draft a non-disclosure agreement (NDA) between Company C and Contractor D.
2. Ensure that the NDA includes clauses for confidentiality, term of agreement, governing law, and dispute resolution.
3. The term of the agreement should be for 2 years, the governing law should be State Z, and disputes should be resolved through mediation.
4. Ensure that your draft is coherent and legally accurate.

Your response should be in the following format:
Drafted Document:
[Your drafted NDA]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'document_text' in t:
            criteria = ["The submission should correctly identify the clauses for Delivery Date, Payment Terms, Governing Law, and Dispute Resolution from the given document."]
        elif 'draft_criteria' in t:
            criteria = ["The drafted NDA should include clauses for confidentiality, term of agreement (2 years), governing law (State Z), and dispute resolution (mediation).", "The drafted document should be coherent and legally accurate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
