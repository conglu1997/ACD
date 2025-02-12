class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"document": "This contract is between Party A and Party B. Party A agrees to provide consulting services to Party B for a period of 12 months, starting from the date of signing. Party B agrees to pay Party A a monthly fee of $5000. Either party may terminate this contract with a 30-day written notice. In case of termination, Party B will pay Party A for the services rendered up to the termination date.", "scenario": "Party B decides to terminate the contract after 6 months and gives a 30-day notice. How much should Party B pay Party A, including the notice period, if the notice is given at the end of the 6th month?"},
            "2": {"document": "This lease agreement is made between the Landlord and the Tenant. The Landlord agrees to lease the property located at 123 Main Street to the Tenant for a period of 1 year, starting from January 1st. The monthly rent is $1000, payable on the first day of each month. Late payments will incur a fee of $50 per day. The Tenant may not sublease the property without the Landlord's written consent.", "scenario": "The Tenant fails to pay rent on February 1st and pays on February 10th instead. How much should the Tenant pay, including late fees, if this happens for two consecutive months?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following legal document and apply the information to the given scenario:\n\nLegal Document:\n{t['document']}\n\nScenario:\n{t['scenario']}\n\nProvide a detailed and accurate answer based on the information in the legal document. Submit your response as a plain text string, clearly stating the amount to be paid and explaining the calculation."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should correctly interpret the legal document.",
            "The response should provide a detailed and accurate answer to the scenario based on the legal document.",
            "The response should clearly state the amount to be paid and explain the calculation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
