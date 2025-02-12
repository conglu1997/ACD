class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "document": """This Agreement is made and entered into as of [Date] by and between [Party A], located at [Address], and [Party B], located at [Address]. WHEREAS, [Party A] is engaged in the business of [Business Description], and WHEREAS, [Party B] desires to obtain services from [Party A] in connection with [Service Description], NOW, THEREFORE, in consideration of the mutual agreements contained herein, the parties hereto agree as follows: 1. Services. [Party A] agrees to provide [Party B] with [Service Details]. 2. Payment. [Party B] agrees to pay [Party A] [Payment Terms]. 3. Term and Termination. This Agreement shall commence on [Start Date] and continue until [End Date], unless terminated earlier in accordance with this Agreement. 4. Confidentiality. Both parties agree to maintain the confidentiality of any proprietary information disclosed under this Agreement. 5. Governing Law. This Agreement shall be governed by and construed in accordance with the laws of [State/Country]. 6. Dispute Resolution. Any disputes arising from this Agreement shall be resolved through binding arbitration in [Location]."""
            },
            "2": {
                "document": """This Lease Agreement is made and entered into as of [Date] by and between [Landlord], located at [Address], and [Tenant], located at [Address]. WHEREAS, [Landlord] is the owner of certain real property located at [Property Address], and WHEREAS, [Tenant] desires to lease the property from [Landlord] on the terms and conditions set forth herein, NOW, THEREFORE, in consideration of the mutual covenants and promises herein contained, the parties hereto agree as follows: 1. Premises. [Landlord] hereby leases to [Tenant] the premises located at [Property Address]. 2. Term. The term of this lease shall commence on [Start Date] and shall continue until [End Date]. 3. Rent. [Tenant] agrees to pay [Landlord] rent in the amount of [Rent Amount] per month, payable in advance on the first day of each month. 4. Security Deposit. [Tenant] shall deposit with [Landlord] the sum of [Deposit Amount] as security for the performance of [Tenant]'s obligations. 5. Maintenance. [Tenant] agrees to maintain the premises in good condition. 6. Governing Law. This Lease shall be governed by and construed in accordance with the laws of [State/Country]. 7. Termination. Either party may terminate this Lease with thirty (30) days written notice to the other party."""
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Summarize the following legal document into a concise and accurate summary. The summary should capture the main points and essential details of the document while maintaining clarity and coherence. Submit your summary as a plain text string.\n\nLegal Document:\n{t['document']}\n\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The summary should accurately reflect the main points of the legal document.",
            "The summary should be concise and coherent.",
            "The summary should maintain the clarity and intent of the original document."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
