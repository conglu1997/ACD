class TaskFamily:
    import re
    
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "clauses": [
                    "This Agreement shall commence on the Effective Date and shall continue in full force and effect until terminated in accordance with the terms of this Agreement.",
                    "Either Party may terminate this Agreement upon providing thirty (30) days' written notice to the other Party.",
                    "Upon termination of this Agreement, each Party shall return or destroy all Confidential Information of the other Party in its possession."
                ],
                "requirements": "Create a termination notice for this agreement, ensuring that it includes the reason for termination and complies with the provided clauses."
            },
            "2": {
                "clauses": [
                    "The Tenant shall pay the Landlord a monthly rent of $1,200, payable in advance on the first day of each calendar month.",
                    "The Landlord shall maintain the premises in a good state of repair and comply with all applicable health and safety regulations.",
                    "The Tenant shall not sublet the premises without the prior written consent of the Landlord."
                ],
                "requirements": "Draft a lease agreement incorporating the above clauses and ensuring it includes standard sections such as parties, term, rent, maintenance, and subletting."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = """Your task is to generate a coherent and legally sound document based on the following provided legal clauses and requirements:\n\n"""
        for clause in t['clauses']:
            instructions += f"- {clause}\n"
        instructions += f"\nRequirements: {t['requirements']}\n"
        instructions += """\nEnsure that your document is clear, accurate, and adheres to the provided clauses. Provide your document in plain text format. Your response should be structured as follows:\n\n[Document Title]\n[Body of the document]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The document should be coherent and logically structured.",
            "The document should accurately incorporate the provided legal clauses.",
            "The document should comply with the specified requirements.",
            "The language used should be formal and appropriate for a legal document."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
