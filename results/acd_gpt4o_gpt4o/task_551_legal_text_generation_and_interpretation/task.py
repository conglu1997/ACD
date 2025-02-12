class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"requirements": "Draft a non-disclosure agreement (NDA) between two parties where Party A shares confidential information with Party B. Ensure to include clauses on confidentiality, duration (2 years), exclusions (information already public or obtained independently), and obligations upon termination."},
            "2": {"scenario": "Party A and Party B entered into a contract where Party B agreed to deliver 100 units of goods to Party A by June 1st. Party A claims that Party B has breached the contract by delivering the goods on June 10th. Interpret the scenario and advise Party A on the potential legal remedies available, considering whether time was of the essence in the contract."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'requirements' in t:
            return f"""Your task is to draft a legal contract based on the following requirements:\n\n{t['requirements']}\n\nEnsure that the contract is comprehensive, legally accurate, and follows common legal standards. Provide your response in plain text format."""
        elif 'scenario' in t:
            return f"""Your task is to interpret the following legal scenario and provide appropriate legal advice:\n\n{t['scenario']}\n\nEnsure that your advice is clear, legally sound, and considers potential legal remedies. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'requirements' in t:
            criteria = ["The contract should be comprehensive and include all specified clauses.", "The contract should be legally accurate and follow common legal standards."]
        else:
            criteria = ["The legal advice should be clear and legally sound.", "The advice should consider potential legal remedies."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
