class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A tenant is facing eviction due to non-payment of rent. The tenant claims that the landlord has failed to make necessary repairs to the property, which has made it uninhabitable. The tenant wants to know their legal rights and potential actions they can take."},
            "2": {"scenario": "An employee has been terminated from their job without any prior notice or reason given by the employer. The employee believes the termination was unjust and wants to know what legal recourse they have."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        return f"""Based on the following scenario, provide legal advice that is relevant, accurate, and considers applicable laws and principles:\n\nScenario:\n{scenario}\n\nProvide your response in the following format:\n\nLegal Advice: [Your legal advice]\nExplanation: [A detailed explanation of the legal reasoning and principles behind your advice]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The legal advice should be relevant and accurate.", "The explanation should be logical and based on applicable laws and principles."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
