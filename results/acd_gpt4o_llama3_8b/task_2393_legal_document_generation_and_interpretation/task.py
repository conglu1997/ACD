class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "contract", "details": "Create a non-disclosure agreement (NDA) between two parties, outlining the obligations of confidentiality, the scope of confidential information, the duration of the agreement, and any exclusions from confidentiality."},
            "2": {"type": "interpretation", "document": "This is a sample legal document: 'The lessee agrees to pay the lessor the sum of $1000 per month as rent for the premises located at 123 Main St, Anytown, USA, for a term of one year commencing on January 1, 2023, and ending on December 31, 2023. The lessee shall also be responsible for all utilities and maintenance of the property.'", "task": "Explain the obligations of the lessee and lessor in this agreement."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "contract":
            return f"""Generate a legal contract based on the following criteria:\n\nDetails: {t['details']}\n\nYour contract should include the following sections:\n1. Introduction: Define the parties involved.\n2. Definitions: Scope of confidential information.\n3. Obligations: Duties of each party regarding confidentiality.\n4. Duration: Time period of the agreement.\n5. Exclusions: Information not covered by the agreement.\n6. Miscellaneous: Any additional clauses.\n\nEnsure the contract is formatted in a professional legal document style. Submit your contract as a plain text string in the following format:\n\n[Contract Body]"""
        elif t["type"] == "interpretation":
            return f"""Interpret the following legal document and explain the obligations of each party involved:\n\nDocument: {t['document']}\n\nYour explanation should cover the following points:\n1. Lessee's Obligations\n2. Lessor's Obligations\n\nSubmit your explanation as a plain text string in the following format:\n\n1. Lessee's Obligations: [Your explanation]\n2. Lessor's Obligations: [Your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "contract":
            criteria = ["The contract should include all necessary sections.", "The contract should be formatted in a professional legal document style."]
        elif t["type"] == "interpretation":
            criteria = ["The explanation should cover all the obligations mentioned in the document."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
