class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "analyze", "document": "This is a sample contract clause: 'The Contractor shall complete the work by December 31, 2023. If the Contractor fails to complete the work by this date, they shall be liable for liquidated damages in the amount of $500 per day of delay.'"},
            "2": {"task_type": "generate", "scenario": "Create a new confidentiality agreement clause that ensures both parties do not disclose any proprietary information to third parties."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'analyze':
            return f"""Your task is to analyze the given contract clause and provide a detailed explanation of its components and legal implications.

Contract Clause: {t['document']}

Instructions:
1. Break down the clause into its essential components.
2. Explain the legal implications of each component.
3. Discuss any potential issues or ambiguities in the clause.

Your response should be structured as follows:
1. Components: [List of components]
2. Legal Implications: [Explanation of legal implications]
3. Potential Issues: [Discussion of potential issues]"""
        elif t['task_type'] == 'generate':
            return f"""Your task is to generate a new confidentiality agreement clause based on the given scenario.

Scenario: {t['scenario']}

Instructions:
1. Create a detailed confidentiality agreement clause that aligns with the given scenario.
2. Ensure that the clause covers all necessary legal aspects.
3. The clause should be clear, concise, and legally sound.

Your response should be in the following format:
Confidentiality Clause: [Your clause]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'analyze':
            criteria = ["The analysis should break down the clause into essential components.", "The explanation should cover the legal implications of each component.", "The discussion should identify any potential issues or ambiguities.", "The analysis should be coherent and insightful."]
        elif t['task_type'] == 'generate':
            criteria = ["The confidentiality clause should align with the given scenario.", "The clause should cover all necessary legal aspects.", "The clause should be clear, concise, and legally sound."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
