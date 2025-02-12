class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "contract": "This Agreement is made and entered into as of [Date] by and between [Company A], a [State] corporation with its principal office located at [Address] (hereinafter referred to as 'Company A'), and [Company B], a [State] corporation with its principal office located at [Address] (hereinafter referred to as 'Company B').\n\n1. Term: The term of this Agreement shall commence on the date hereof and shall continue for a period of one (1) year unless terminated earlier in accordance with the provisions of this Agreement.\n\n2. Services: Company A agrees to provide Company B with the following services: [Describe Services].\n\n3. Compensation: Company B agrees to pay Company A the sum of [Amount] for the services provided under this Agreement. Payment shall be made in [Number] installments of [Amount], due on the [Date] of each month.\n\n4. Confidentiality: Both parties agree to maintain the confidentiality of any proprietary information disclosed during the term of this Agreement.\n\n5. Termination: Either party may terminate this Agreement upon thirty (30) days written notice to the other party.\n\n6. Governing Law: This Agreement shall be governed by and construed in accordance with the laws of the State of [State].\n\n7. Miscellaneous: This Agreement constitutes the entire agreement between the parties and supersedes all prior agreements and understandings, whether written or oral, relating to the subject matter hereof.",
                "question": "Identify any potential issues or ambiguities in the provided contract and suggest improvements to address them. Provide your response in a clear and structured format."
            },
            "2": {
                "contract": "This Consulting Agreement (the 'Agreement') is entered into as of [Date], by and between [Consultant], an individual with a principal place of business at [Address] ('Consultant'), and [Client], a [State] corporation with its principal place of business at [Address] ('Client').\n\n1. Services: Consultant agrees to provide the following services to Client: [Describe Services].\n\n2. Compensation: Client agrees to pay Consultant the sum of [Amount] per hour for services rendered under this Agreement. Invoices shall be submitted monthly and payment shall be due within thirty (30) days of receipt.\n\n3. Independent Contractor: Consultant shall perform the services as an independent contractor and not as an employee of Client. Consultant shall have no authority to bind Client in any manner.\n\n4. Confidentiality: Consultant agrees to maintain the confidentiality of any proprietary information disclosed by Client.\n\n5. Term and Termination: This Agreement shall commence on the date hereof and continue until terminated by either party upon thirty (30) days written notice.\n\n6. Governing Law: This Agreement shall be governed by and construed in accordance with the laws of the State of [State].\n\n7. Entire Agreement: This Agreement constitutes the entire agreement between the parties and supersedes all prior agreements, understandings, and representations, whether written or oral.",
                "question": "Review the provided consulting agreement and identify any potential legal or practical issues. Suggest improvements to enhance clarity and effectiveness. Provide your response in a clear and structured format."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the following legal contract and identify any potential issues or ambiguities. Suggest improvements to address these issues and enhance the clarity and effectiveness of the contract. Provide your response in a clear and structured format.\n\nContract:\n{t['contract']}\n\nQuestion:\n{t['question']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
