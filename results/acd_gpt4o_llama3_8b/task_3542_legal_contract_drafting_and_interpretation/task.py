class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A freelance graphic designer is hired to create a logo for a startup company. Draft a contract that outlines the scope of work, payment terms, intellectual property rights, and any other relevant clauses.",
                "requirements": [
                    "Scope of Work: Describe the specific tasks and deliverables.",
                    "Payment Terms: Outline the payment schedule and amounts.",
                    "Intellectual Property: Specify the ownership and usage rights of the created logo.",
                    "Other Clauses: Include any additional clauses relevant to the agreement."
                ]
            },
            "2": {
                "contract": "This Agreement is made this [date] by and between [Party A] and [Party B], collectively referred to as 'the Parties'. Party A agrees to provide consulting services to Party B under the following terms: 1. Scope of Services: Party A will provide consulting services related to [specific area]. 2. Compensation: Party B agrees to pay Party A [amount] per hour for the services provided. 3. Confidentiality: Both Parties agree to maintain the confidentiality of any proprietary information shared during the term of this Agreement. 4. Termination: This Agreement may be terminated by either Party with [number] days written notice. 5. Governing Law: This Agreement shall be governed by the laws of [state/country].",
                "requirements": [
                    "Identify the key clauses in the contract.",
                    "Interpret the obligations and rights of each party based on the provided contract."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'scenario' in t:
            return f"""Draft a legal contract based on the following scenario: {t['scenario']}

The contract should include the following elements:
1. Scope of Work: Describe the specific tasks and deliverables.
2. Payment Terms: Outline the payment schedule and amounts.
3. Intellectual Property: Specify the ownership and usage rights of the created logo.
4. Other Clauses: Include any additional clauses relevant to the agreement.

Submit your contract as a plain text string in a structured and clear format."""
        else:
            return f"""Interpret the following legal contract and provide a detailed analysis of the key clauses and the obligations and rights of each party:

Contract: '{t['contract']}'

Your analysis should identify the key clauses and explain the obligations and rights of each party based on the provided contract. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if 'scenario' in t:
            criteria = [
                "The contract should include a clear and detailed scope of work.",
                "The contract should outline the payment terms accurately.",
                "The contract should specify the intellectual property rights clearly.",
                "The contract should include any additional relevant clauses."
            ]
        else:
            criteria = [
                "The analysis should identify the key clauses in the contract.",
                "The analysis should explain the obligations and rights of each party based on the provided contract."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
