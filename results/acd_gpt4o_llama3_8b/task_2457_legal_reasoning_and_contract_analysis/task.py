class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "contract": "This Employment Agreement ('Agreement') is made effective as of January 1, 2022, by and between ABC Corporation ('Employer') and John Doe ('Employee'). 1. Employment: Employer agrees to employ Employee as a Senior Software Engineer. Employee accepts employment with Employer on the terms and conditions set forth in this Agreement. 2. Compensation: Employee will be paid an annual salary of $120,000, payable in accordance with Employer's standard payroll practices. 3. Termination: This Agreement may be terminated by either party upon thirty (30) days' written notice. In the event of termination, Employee shall be entitled to payment for all work performed up to the date of termination."
            },
            "2": {
                "contract": "This Non-Disclosure Agreement ('Agreement') is entered into as of August 1, 2022, by and between XYZ Innovations ('Disclosing Party') and Jane Smith ('Receiving Party'). 1. Confidential Information: For purposes of this Agreement, 'Confidential Information' includes all written, electronic, or oral information disclosed by the Disclosing Party to the Receiving Party. 2. Obligations of Receiving Party: Receiving Party agrees to hold and maintain the Confidential Information in strictest confidence for the sole and exclusive benefit of the Disclosing Party. 3. Term: This Agreement and Receiving Party’s duty to hold Confidential Information in confidence shall remain in effect until the Confidential Information no longer qualifies as confidential or until Disclosing Party sends written notice releasing Receiving Party from this Agreement."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Read the following legal contract and answer the questions below:

Contract:
{t['contract']}

Questions:
1. Identify the key clauses in this contract and explain their significance.
2. Are there any potential legal risks or ambiguities in this contract? If so, describe them.

Submit your response as a plain text string in the following format:

Key Clauses: [Your identification and explanation here]
Legal Risks/Ambiguities: [Your identification and description here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The key clauses should be accurately identified and their significance explained.",
            "Any potential legal risks or ambiguities should be identified and described clearly."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
