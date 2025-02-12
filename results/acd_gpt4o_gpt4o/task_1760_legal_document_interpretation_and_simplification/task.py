class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "interpret", "document": """This Agreement, made and entered into as of the date set forth below, by and between the Lessor and the Lessee, collectively referred to as the 'Parties', witnesseth that the Lessor hereby leases to the Lessee the premises described herein, subject to the terms and conditions set forth in this Agreement. The Lessee agrees to pay the rent specified and to comply with all covenants and conditions imposed upon the Lessee herein. Failure to comply with any of the terms of this Agreement may result in termination of the lease and eviction. Additionally, the Lessee shall be responsible for maintaining the premises in good condition and shall not engage in any activities that violate local laws and ordinances."""},
            "2": {"task_type": "simplify", "document": """In accordance with the provisions of this Act, any person found guilty of the offense of larceny shall be liable to imprisonment for a term not exceeding five years or to a fine not exceeding ten thousand dollars, or both. The term 'larceny' shall include theft, burglary, and any other form of unlawful taking of property as defined by this Act. Furthermore, repeat offenders shall be subject to enhanced penalties, including longer imprisonment terms and higher fines."""}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'interpret':
            return f"""Your task is to interpret the following legal document and explain its meaning in simple, clear language. Ensure that your explanation captures all key elements and is accessible to someone without a legal background.\n\nDocument:\n{t['document']}\n\nProvide your explanation in plain text format."""
        elif t['task_type'] == 'simplify':
            return f"""Your task is to simplify the following legal statement. Rewrite it in plain, clear language that anyone without legal training can understand while preserving the original meaning.\n\nDocument:\n{t['document']}\n\nProvide your simplified version in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should accurately capture the key elements of the original document.", "The language used should be clear and accessible to a layperson."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
