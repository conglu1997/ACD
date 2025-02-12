class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "document": "A contract between two parties, Company A and Company B, states the following: 'Company A agrees to deliver 100 units of product X to Company B by the 15th of each month. In case of delay, Company A will pay a penalty of $500 per day of delay. The contract is valid for one year and can be renewed upon mutual agreement.'\n\nScenario: Company A delivers the product on the 20th of the month. Determine the penalty and explain the reasoning.",
                "question": "What is the penalty amount and the reasoning?"
            },
            "2": {
                "document": "A will states: 'I, John Doe, bequeath my house to my daughter Jane Doe, and the remainder of my estate to my son Jack Doe. If either of my children predeceases me, their share shall pass to their descendants.'\n\nScenario: Jane Doe predeceased John Doe, leaving two children. Explain how the estate should be distributed.",
                "question": "How should the estate be distributed and why?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following legal document and provide a detailed response to the scenario.\n\nDocument:\n{t['document']}\n\nScenario:\n{t['question']}\n\nFormat your response as follows:\n- Penalty/Distribution: [Your answer] \n- Reasoning: [Your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should correctly interpret the legal document.",
            "The response should provide a correct and logical reasoning based on the document.",
            "The response should be clear and precise."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
