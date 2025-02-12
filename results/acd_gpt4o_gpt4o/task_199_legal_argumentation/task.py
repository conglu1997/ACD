class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A tenant is being evicted for non-payment of rent. The tenant claims they withheld rent because the landlord failed to make necessary repairs. Develop legal arguments for both the tenant and the landlord."},
            "2": {"scenario": "An employee was terminated for alleged misconduct. The employee claims they were wrongfully terminated due to discrimination. Develop legal arguments for both the employee and the employer."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the following legal scenario and generate appropriate legal arguments for both sides:

Scenario: {t["scenario"]}

Provide clear, detailed, and logically structured arguments for each side. Ensure that your arguments are based on relevant legal principles and consider possible counterarguments. Provide your response in plain text format, structured as follows:

1. Arguments for Side A
2. Arguments for Side B
3. Possible counterarguments and responses for each side."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The arguments should be clear and detailed.", "The arguments should be logically structured.", "The arguments should be based on relevant legal principles.", "The arguments should consider possible counterarguments."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
