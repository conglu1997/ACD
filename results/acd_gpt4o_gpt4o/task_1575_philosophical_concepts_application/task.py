class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theory": "Utilitarianism", "scenario": "A government must decide whether to sacrifice a small village to save a larger city from a natural disaster. Explain how a utilitarian would approach this decision and justify it."},
            "2": {"theory": "Deontology", "scenario": "A doctor must decide whether to lie to a patient to prevent them from experiencing distress. Explain how a deontologist would approach this decision and justify it."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to explain and apply the philosophical theory of {t["theory"]} to the following scenario: {t["scenario"]}. Ensure your explanation is detailed and clearly shows how the theory applies to the scenario. Provide your response in plain text format.

Format your response as follows:
Explanation: [Your detailed explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should accurately represent the philosophical theory.", "The application of the theory to the scenario should be logical and well-justified.", "The response should follow the specified format.", "The response should be detailed and clearly show how the theory applies to the scenario."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
