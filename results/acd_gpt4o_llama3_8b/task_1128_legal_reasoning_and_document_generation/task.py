class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are given the following legal text: 'No person shall operate a motor vehicle while under the influence of alcohol or drugs.' Your task is to interpret this law and explain its implications in a case where a person was found operating a motor vehicle with a blood alcohol concentration (BAC) of 0.08% in a state where the legal limit is 0.08%. Provide a detailed explanation of the legal interpretation and possible outcomes."},
            "2": {"scenario": "Draft a legally binding rental agreement for an apartment. The agreement should include terms such as rent amount, lease duration, tenant and landlord responsibilities, and any other essential clauses to ensure a comprehensive and enforceable contract. Assume the rent amount is $1200 per month, and the lease duration is one year."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t['scenario']
        return f"""Complete the following task based on the given scenario:

Scenario: {scenario}

For Task 1, provide a detailed interpretation of the legal text and its implications in the given case. Ensure your explanation is thorough and logically sound. For Task 2, draft a legally binding rental agreement that includes all necessary terms and clauses for a comprehensive contract. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The interpretation should be thorough and logically sound.", "The rental agreement should include all necessary terms and clauses."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
