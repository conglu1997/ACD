class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"symptoms": ["fever", "cough", "shortness of breath", "loss of taste", "fatigue", "rash", "conjunctivitis"]},
            "2": {"condition": "Type 2 Diabetes"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'symptoms' in t:
            return f"""Your task is to diagnose the medical condition based on the following symptoms:

Symptoms: {', '.join(t['symptoms'])}

Provide your diagnosis in plain text format as follows:
Diagnosis: [Your diagnosis]"""
        elif 'condition' in t:
            return f"""Your task is to provide a step-by-step action plan for managing the following medical condition:

Condition: {t['condition']}

Ensure that your action plan is practical, safe, coherent, and evidence-based. Provide your response in plain text format as follows:
Action Plan: [Your step-by-step action plan]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'symptoms' in t:
            criteria = [
                "The diagnosis should be medically accurate based on the given symptoms.",
                "The diagnosis should consider all provided symptoms."
            ]
        else:
            criteria = [
                "The action plan should be practical and safe for managing the given condition.",
                "The action plan should be coherent and detailed.",
                "The action plan should be evidence-based."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
