class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "parameters": {
                    "parties": ["Alice", "Bob"],
                    "agreement_type": "Non-Disclosure Agreement (NDA)",
                    "effective_date": "2023-10-01",
                    "confidential_information": "any proprietary information disclosed in written or oral form",
                    "duration": "2 years",
                    "jurisdiction": "State of California"
                }
            },
            "2": {
                "contract": "This Employment Agreement is made effective as of August 1, 2023, by and between XYZ Corp (the 'Employer') and John Doe (the 'Employee'). WHEREAS, the Employer desires to employ the Employee and the Employee desires to accept such employment, both parties agree to the following terms: 1. Job Title: The Employee will serve as 'Software Engineer'. 2. Compensation: The Employee will be paid an annual salary of $100,000. 3. Termination: Either party may terminate this agreement with 30 days' notice. 4. Confidentiality: The Employee agrees to maintain the confidentiality of the Employer's proprietary information."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "parameters" in t:
            params = t["parameters"]
            instructions = (
                f"Your task is to generate a legal contract based on the following parameters:\n"
                f"Parties: {', '.join(params['parties'])}\n"
                f"Agreement Type: {params['agreement_type']}\n"
                f"Effective Date: {params['effective_date']}\n"
                f"Confidential Information: {params['confidential_information']}\n"
                f"Duration: {params['duration']}\n"
                f"Jurisdiction: {params['jurisdiction']}\n"
                "\nEnsure the contract is coherent, legally sound, and contains the necessary clauses typical for the specified agreement type. Submit your contract in plain text format."
            )
        else:
            contract = t["contract"]
            instructions = (
                f"Your task is to interpret the following legal contract clause:\n"
                f"{contract}\n"
                "\nProvide a detailed explanation of the clause, including the obligations of each party and any important legal implications. Submit your interpretation in plain text format."
            )
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "parameters" in t:
            criteria = [
                "The contract should be coherent and legally sound.",
                "The contract should include all provided parameters.",
                "The contract should contain necessary clauses typical for the specified agreement type."
            ]
        else:
            criteria = [
                "The interpretation should accurately describe the obligations of each party.",
                "The interpretation should highlight any important legal implications.",
                "The interpretation should be clear and precise."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
