class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A freelance graphic designer is entering into a contract with a client to design a logo. The contract should include terms related to payment, deliverables, deadlines, and intellectual property rights."},
            "2": {"scenario": "A software developer is entering into a contract with a company to develop a custom software application. The contract should include terms related to project scope, payment milestones, confidentiality, and maintenance."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a legal contract based on the following scenario:

Scenario: {t['scenario']}

Ensure that the contract includes all necessary terms and conditions relevant to the scenario. The contract should be clearly structured and use appropriate legal terminology. Provide your contract in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The contract should include appropriate terms and conditions relevant to the scenario.", "The contract should be clearly structured and use appropriate legal terminology."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
