class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "Draft a confidentiality clause for a contract between two companies, Company A and Company B. The clause should ensure that both parties agree to keep any shared proprietary information confidential for a period of three years. Additionally, the clause should specify what constitutes proprietary information and outline any exceptions to the confidentiality obligation."
            },
            "2": {
                "scenario": "Interpret the following legal clause and explain its implications in simple terms: 'Notwithstanding any other provision of this Agreement, either party may terminate this Agreement immediately upon written notice if the other party becomes insolvent, makes an assignment for the benefit of creditors, or is subject to any proceeding under bankruptcy or insolvency law.' Provide an example scenario where this clause might be invoked."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given scenario:

Scenario: {t['scenario']}

For Task 1, draft a legal clause that meets the requirements outlined in the scenario. The clause should be precise, legally sound, and appropriate for the given context. Ensure it includes all necessary details specified in the scenario.
For Task 2, interpret the given legal clause and explain its implications in simple terms. Additionally, provide an example scenario where this clause might be invoked.

Ensure that your response is precise, legally sound, and appropriate for the given context.

Submit your response as a plain text string in the following format:

Task 1:
[Your drafted legal clause here]

Task 2:
[Your interpretation and example scenario here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The response should be legally sound and appropriate for the given context.", "The response should be precise and clear.", "The response for Task 1 should include all necessary details specified in the scenario.", "The response for Task 2 should include an example scenario where the clause might be invoked."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
