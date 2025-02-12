class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"symptoms": "A 45-year-old male presents with chest pain, shortness of breath, sweating, and nausea. The pain radiates to the left arm and jaw, and he has a history of hypertension."},
            "2": {"symptoms": "A 30-year-old female presents with a persistent cough, fever, night sweats, and fatigue. She has experienced significant weight loss over the past two months and has a history of travel to regions with high TB prevalence."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following symptoms, provide a plausible medical diagnosis and suggest a treatment plan. Ensure that your response includes:
1. A clear diagnosis.
2. A detailed explanation of the diagnosis.
3. A suggested treatment plan.
4. Any necessary follow-up actions or precautions.

Symptoms: {t["symptoms"]}

Submit your response as a plain text string in the following format:
Diagnosis: [Your diagnosis]
Explanation: [Detailed explanation]
Treatment Plan: [Suggested treatment plan]
Follow-Up Actions: [Any necessary follow-up actions or precautions]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include a clear medical diagnosis.", "The response should include a detailed explanation of the diagnosis.", "The response should include a suggested treatment plan.", "The response should include any necessary follow-up actions or precautions.", "The diagnosis and treatment plan should be plausible and medically sound.", "The response should follow the specified format exactly."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
