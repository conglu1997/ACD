class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"document": "This Lease Agreement (\"Agreement\") is made and entered into on this 1st day of January, 2023, by and between John Doe (\"Landlord\") and Jane Smith (\"Tenant\"). The Landlord hereby leases to the Tenant and the Tenant hereby leases from the Landlord the premises located at 123 Main Street, Springfield, for a term commencing on January 1, 2023, and ending on December 31, 2023, under the following terms and conditions: 1. Rent: The Tenant agrees to pay the Landlord as rent for the premises the sum of $1,000 per month, payable in advance on the first day of each month. 2. Security Deposit: The Tenant shall deposit with the Landlord the sum of $1,000 as security for the full and faithful performance by the Tenant of all the terms of this Agreement..."},
            "2": {"requirements": "Draft a simple non-disclosure agreement (NDA) for a company (ABC Corp) and an individual contractor (John Doe). The NDA should include the following sections: 1. Definition of Confidential Information 2. Obligations of Receiving Party 3. Exclusions from Confidential Information 4. Term 5. Governing Law"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'document' in t:
            return f"""Your task is to analyze the following legal document and extract the key provisions:

{t['document']}

Provide a summary of the key provisions in plain text format, ensuring clarity and accuracy. Your response should be in the following format:
Summary: [Your summary]"""
        else:
            return f"""Your task is to draft a simple non-disclosure agreement (NDA) based on the following requirements:

{t['requirements']}

Ensure that the NDA includes all the specified sections and is written in clear and concise legal language. Provide the complete NDA in plain text format. Your response should be in the following format:
NDA: [Your NDA]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'document' in t:
            criteria = ["The summary should accurately reflect the key provisions of the document.", "The summary should be clear and concise."]
        else:
            criteria = ["The NDA should include all specified sections.", "The NDA should be written in clear and concise legal language.", "The NDA should follow a logical structure and be legally sound."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
