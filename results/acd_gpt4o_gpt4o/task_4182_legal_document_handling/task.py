class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are provided with a legal contract for a rental agreement. Identify any potential issues or points of concern in the contract and suggest improvements.", "contract": "This Rental Agreement is made this 1st day of January, 2023, between John Doe (Landlord) and Jane Smith (Tenant). The Landlord agrees to rent the premises located at 123 Main St, Cityville, to the Tenant for a period of 12 months commencing on the 1st day of January, 2023, at a monthly rent of $1000. The Tenant agrees to pay the rent on the 1st day of each month. The Tenant shall not sublet the premises without the written consent of the Landlord. The Tenant shall be responsible for all utilities. The Landlord may terminate this agreement with a 30-day notice.", "requirements": "Identify at least three potential issues or areas of concern in the contract and suggest specific improvements for each."},
            "2": {"scenario": "Draft a simple will for an individual based on the provided information.", "information": "Name: Sarah Johnson. Assets: House at 456 Elm St, Car, Savings account with $50,000. Beneficiaries: House to son Michael Johnson, Car to daughter Emily Johnson, Savings account to be equally divided between Michael and Emily. Executor: Sarah's brother, Robert Johnson.", "requirements": "Create a will that clearly outlines the distribution of assets according to the provided information. Ensure that the will is legally sound and includes all necessary components."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "contract" in t:
            return f"""Your task is to analyze the provided rental agreement contract and identify any potential issues or points of concern. Suggest specific improvements for each identified issue.

Contract: {t['contract']}

Your response should include:
1. Identification of at least three potential issues or areas of concern in the contract.
2. Specific improvements or modifications to address each identified issue.

Provide your response in plain text format."""
        elif "information" in t:
            return f"""Your task is to draft a simple will based on the provided information.

Information: {t['information']}

Your response should include:
1. A clear and legally sound will that outlines the distribution of assets according to the provided information.
2. Inclusion of all necessary components of a will.

Provide your response in plain text format."""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "contract" in t:
            criteria = [
                "The identified issues or areas of concern should be valid and relevant.",
                "The suggested improvements should be specific and address the identified issues.",
                "The response should demonstrate a clear understanding of legal contracts and potential pitfalls."
            ]
        elif "information" in t:
            criteria = [
                "The will should clearly outline the distribution of assets according to the provided information.",
                "The will should be legally sound and include all necessary components.",
                "The response should demonstrate a clear understanding of the structure and requirements of a will."
            ]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
