class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "contract": "This Employment Agreement (\"Agreement\") is made between Employer, Inc. (\"Employer\") and John Doe (\"Employee\"). The Employer agrees to hire the Employee for a period of one year, starting from January 1, 2023. The Employee will be responsible for managing the sales department and meeting quarterly sales targets. The Employee will receive an annual salary of $60,000, paid in monthly installments. The Employee is entitled to two weeks of paid vacation per year. The Employee agrees to adhere to the company's policies and maintain confidentiality of proprietary information. Either party may terminate this Agreement with a 30-day written notice. In the event of a dispute arising from this Agreement, both parties agree to first seek mediation before resorting to litigation.",
                "criteria": "Identify the key elements of the contract, including the parties involved, duration, responsibilities, compensation, benefits, termination conditions, and dispute resolution mechanism." 
            },
            "2": {
                "contract": "This Lease Agreement (\"Agreement\") is made between Landlord, LLC (\"Landlord\") and Jane Smith (\"Tenant\"). The Landlord agrees to lease the property located at 123 Main Street to the Tenant for a period of 12 months, starting from February 1, 2023. The monthly rent is $1,200, payable on the first day of each month. The Tenant is responsible for paying all utilities. The Tenant agrees to maintain the property in good condition and not to make any alterations without the Landlord's consent. The Landlord is responsible for major repairs. Either party may terminate this Agreement with a 60-day written notice. In the event of a dispute arising from this Agreement, both parties agree to arbitration as the method of dispute resolution.",
                "criteria": "Identify the key elements of the contract, including the parties involved, duration, rent amount, tenant responsibilities, landlord responsibilities, termination conditions, and dispute resolution mechanism."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the given legal contract and identify its key elements. Ensure your analysis is thorough and includes specific details from the contract. Provide your response in plain text format.\n\nContract: {t['contract']}\nCriteria: {t['criteria']}\n\nResponse format:\n1. Parties Involved: [List the parties involved]\n2. Duration: [Specify the duration of the contract]\n3. Responsibilities: [Detail the responsibilities of each party]\n4. Compensation/Benefits: [Specify the compensation and any benefits]\n5. Termination Conditions: [Detail the termination conditions]\n6. Dispute Resolution: [Specify the dispute resolution mechanism]\n\nExample response:\n1. Parties Involved: Employer, Inc. (Employer) and John Doe (Employee)\n2. Duration: One year, starting from January 1, 2023\n3. Responsibilities: Employee responsible for managing the sales department and meeting quarterly sales targets; Employee to adhere to company policies and maintain confidentiality\n4. Compensation/Benefits: Annual salary of $60,000, paid in monthly installments; two weeks of paid vacation per year\n5. Termination Conditions: Either party may terminate with a 30-day written notice\n6. Dispute Resolution: Mediation before litigation."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should be thorough and include specific details from the contract.",
            "The response should follow the specified format.",
            "The response should accurately identify the key elements of the contract based on the criteria."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
