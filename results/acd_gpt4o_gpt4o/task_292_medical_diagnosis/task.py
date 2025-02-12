class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"symptoms": "A 45-year-old male presents with chest pain, shortness of breath, and sweating. He reports that the pain is severe and radiates to his left arm. He has a history of hypertension and high cholesterol. The pain started suddenly while he was resting."},
            "2": {"symptoms": "A 30-year-old female presents with severe, sudden onset abdominal pain, nausea, and vomiting. The pain is located in the lower right quadrant of her abdomen. She has a low-grade fever and tenderness in the lower right abdomen, especially upon release of pressure. She denies any recent trauma."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to diagnose the medical condition based on the following symptoms:

{t["symptoms"]}

Provide your diagnosis in plain text format, along with a brief explanation of your reasoning. Format your response as follows:

Diagnosis: [Your diagnosis]
Explanation: [Your detailed explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should clearly state a plausible medical diagnosis.",
            "The response should provide a detailed explanation of the reasoning based on the given symptoms.",
            "The response should use correct medical terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
