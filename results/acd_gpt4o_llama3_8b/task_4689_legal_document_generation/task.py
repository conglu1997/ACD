class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"document_type": "Non-Disclosure Agreement (NDA)", "parties": ["Company A", "Employee B"], "purpose": "To protect confidential information shared during employment.", "key_clauses": ["Definition of Confidential Information", "Obligations of Receiving Party", "Term and Termination", "Governing Law"]},
            "2": {"document_type": "Lease Agreement", "parties": ["Landlord C", "Tenant D"], "property_address": "123 Elm Street, Anytown, USA", "lease_term": "12 months", "key_clauses": ["Rent Payment", "Security Deposit", "Maintenance and Repairs", "Termination"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Draft a {t['document_type']} based on the following specifications:

Parties: {', '.join(t['parties'])}
Purpose: {t.get('purpose', 'N/A')}
Property Address: {t.get('property_address', 'N/A')}
Lease Term: {t.get('lease_term', 'N/A')}

Include the following key clauses:
- {t['key_clauses'][0]}
- {t['key_clauses'][1]}
- {t['key_clauses'][2]}
- {t['key_clauses'][3]}

Your legal document should be clear, precise, and follow standard legal formatting. After drafting the document, provide a brief summary of each key clause. Submit your response as a plain text string in the following format:

Document: [Your legal document here]

Summary:
- {t['key_clauses'][0]}: [Summary here]
- {t['key_clauses'][1]}: [Summary here]
- {t['key_clauses'][2]}: [Summary here]
- {t['key_clauses'][3]}: [Summary here]

Example:
Document: This Non-Disclosure Agreement ("Agreement") is entered into by and between Company A ("Disclosing Party") and Employee B ("Receiving Party")..."

Summary:
- Definition of Confidential Information: This clause defines what constitutes confidential information under the agreement...
- Obligations of Receiving Party: This clause outlines the responsibilities of the receiving party in handling confidential information...
- Term and Termination: This clause specifies the duration of the agreement and the conditions under which it can be terminated...
- Governing Law: This clause identifies the legal jurisdiction that will govern the agreement..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The legal document should be clear, precise, and follow standard legal formatting.", "The document should include all specified key clauses.", "The summaries should accurately reflect the content of the key clauses."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
