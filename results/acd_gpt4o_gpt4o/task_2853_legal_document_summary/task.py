class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "document": "This Agreement is made and entered into as of [Date], by and between [Party A], a corporation organized and existing under the laws of [State], with its principal place of business at [Address] (hereinafter referred to as 'Company'), and [Party B], a corporation organized and existing under the laws of [State], with its principal place of business at [Address] (hereinafter referred to as 'Contractor'). The Company desires to retain the services of the Contractor, and the Contractor desires to provide such services, under the terms and conditions set forth herein. NOW, THEREFORE, in consideration of the mutual covenants and promises herein contained, the parties hereto agree as follows: 1. Services. The Contractor agrees to perform the services described in Exhibit A attached hereto (the 'Services'). 2. Compensation. The Company agrees to pay the Contractor for the Services in accordance with the terms set forth in Exhibit B attached hereto. 3. Term. This Agreement shall commence on the date first written above and shall continue in effect until terminated by either party in accordance with the provisions of Section 4 hereof. 4. Termination. Either party may terminate this Agreement at any time upon thirty (30) days' prior written notice to the other party. 5. Confidentiality. The Contractor agrees to maintain in confidence and not to use or disclose any confidential information received from the Company except as necessary to perform the Services. ..." },
            "2": {
                "document": "This Lease Agreement (the 'Agreement') is made and entered into as of [Date], by and between [Landlord], a corporation organized and existing under the laws of [State], with its principal place of business at [Address] (hereinafter referred to as 'Landlord'), and [Tenant], an individual with a principal residence at [Address] (hereinafter referred to as 'Tenant'). Landlord hereby leases to Tenant, and Tenant hereby leases from Landlord, the premises located at [Address] (the 'Premises'), upon the terms and conditions set forth herein. 1. Term. The term of this Agreement shall commence on [Start Date] and shall continue until [End Date], unless earlier terminated in accordance with the provisions of this Agreement. 2. Rent. Tenant agrees to pay to Landlord, without demand, the rent of [Amount] per month, in advance, on or before the first day of each month during the term of this Agreement. 3. Security Deposit. Upon execution of this Agreement, Tenant shall deposit with Landlord the sum of [Amount] as security for Tenant's performance of its obligations under this Agreement. 4. Use of Premises. The Premises shall be used and occupied by Tenant solely for residential purposes and for no other purpose without the prior written consent of Landlord. 5. Maintenance and Repairs. Tenant agrees to maintain the Premises in good condition and repair and to promptly notify Landlord of any damage or need for repairs. ..." }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to summarize the provided legal document, highlighting the key points and implications.

Document:
{t['document']}

Ensure that your summary is clear, concise, and accurately reflects the main terms and conditions of the document. The summary should be between 150 to 200 words. Submit your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The summary should accurately reflect the main terms and conditions of the document.",
                   "The summary should be clear and concise.",
                   "The summary should highlight key points and implications.",
                   "The summary should be between 150 to 200 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
