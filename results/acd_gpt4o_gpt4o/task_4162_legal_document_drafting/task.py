class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "John Doe is filing a lawsuit against XYZ Corp for breach of contract. According to the contract, XYZ Corp was supposed to deliver 100 units of a product by January 1st, but they failed to do so. John is seeking damages for the losses incurred due to the delay. Additionally, John had communicated multiple times with XYZ Corp regarding the delay but received no response. XYZ Corp argues that unforeseen circumstances beyond their control caused the delay."},
            "2": {"scenario": "Jane Smith is preparing a will. She wants to leave her entire estate to her two children, with specific instructions that her daughter, Emily, receives the family home and her son, Michael, receives the remaining assets. She also wants to appoint her brother, Robert, as the executor of the will. Additionally, Jane wants to ensure that a specific amount of money is allocated for the maintenance of the family home."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to draft a legal document based on the provided legal scenario. Ensure that the document is well-structured, uses appropriate legal language, and addresses all necessary legal principles.

Scenario: {t['scenario']}

Provide your response in plain text format. Your response should include:
1. A clear and concise statement of the legal issue.
2. The relevant legal principles and any applicable laws.
3. The main arguments or points that need to be made in the document.
4. The final legal document, properly formatted and complete.

For a lawsuit, structure your document as follows:
- Title: [Title of the lawsuit]
- Parties: [List the parties involved]
- Statement of Facts: [Detail the facts of the case]
- Legal Grounds: [List the legal principles and laws applicable]
- Claim for Relief: [Specify the relief sought]
- Conclusion: [Summarize the document]

For a will, structure your document as follows:
- Title: [Title of the will]
- Parties: [List the parties involved]
- Bequests: [Detail the specific bequests]
- Executor: [Name the executor]
- Additional Provisions: [Any additional provisions]
- Conclusion: [Summarize the document]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The document should be well-structured and use appropriate legal language.",
            "The document should address all necessary legal principles and relevant laws.",
            "The document should accurately reflect the scenario provided.",
            "The document should follow the specified format for the type of legal document."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
