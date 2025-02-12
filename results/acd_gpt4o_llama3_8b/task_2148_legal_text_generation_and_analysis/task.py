class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A lease agreement where the tenant is responsible for minor repairs and maintenance. The landlord is responsible for major structural repairs and ensuring the property is habitable."},
            "2": {"legal_text": "The tenant shall be responsible for all minor repairs and maintenance. The landlord shall cover all minor repairs and maintenance costs. The tenant is responsible for major structural repairs and ensuring the property is habitable."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "scenario" in t:
            return f"Generate a legal clause based on the following scenario: {t['scenario']}. Ensure that the clause is coherent, contextually appropriate, legally sound, and covers all necessary aspects. Submit your response as a plain text string in the following format: 'Clause: [Your generated legal clause]'."
        elif "legal_text" in t:
            return f"Identify any inconsistencies in the following legal text: {t['legal_text']}. Provide a brief explanation for each inconsistency identified and suggest a correction. Submit your response as a plain text string in the following format: 'Inconsistencies: [List of inconsistencies] Explanation: [Brief explanation for each inconsistency] Correction: [Suggested corrections for each inconsistency]'."
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "scenario" in t:
            criteria = [
                "The response should be a coherent and contextually appropriate legal clause.",
                "The response should be legally sound.",
                "The response should cover all necessary aspects mentioned in the scenario."
            ]
        elif "legal_text" in t:
            criteria = [
                "The response should correctly identify inconsistencies in the legal text.",
                "The response should provide a brief explanation for each inconsistency identified.",
                "The response should suggest a correction for each inconsistency identified."
            ]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
