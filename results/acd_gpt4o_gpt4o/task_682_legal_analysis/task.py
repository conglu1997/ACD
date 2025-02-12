class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A company is being sued for breach of contract by a supplier. The company argues that the breach was due to unforeseeable circumstances (force majeure). Provide a legal opinion on whether the company can successfully use the force majeure defense.", "law": "Force majeure refers to unforeseeable circumstances that prevent someone from fulfilling a contract. To successfully invoke force majeure, the event must be unforeseeable, external, and unavoidable."},
            "2": {"scenario": "An employee claims they were wrongfully terminated due to discrimination based on gender. The employer claims the termination was due to performance issues. Provide a legal opinion on the potential outcome based on anti-discrimination laws.", "law": "Anti-discrimination laws prohibit employers from terminating employees based on protected characteristics such as gender. The burden of proof lies with the employee to show that discrimination occurred."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the given legal scenario and provide a reasoned legal opinion based on the provided law or precedent.

Scenario: {t["scenario"]}
Law: {t["law"]}

Your response should be a coherent and logical legal opinion that applies the given law to the scenario. Provide your legal opinion in plain text format without any additional formatting."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The legal opinion should accurately apply the given law to the scenario.",
            "The legal opinion should be coherent and logically structured.",
            "The legal opinion should demonstrate an understanding of legal principles.",
            "The legal opinion should be in plain text format without any additional formatting."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
