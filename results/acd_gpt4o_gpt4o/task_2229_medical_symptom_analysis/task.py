class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"symptoms": "A 45-year-old male experiences chest pain, shortness of breath, and sweating.", "patient_history": "The patient has a history of hypertension and high cholesterol."},
            "2": {"symptoms": "A 30-year-old female presents with a persistent cough, fever, and fatigue.", "patient_history": "The patient recently traveled internationally and has no significant past medical history."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to provide medical advice based on the given symptoms and patient history. Include potential diagnoses and recommended actions. Ensure that your advice is clear, accurate, and considers the patient's history.

Symptoms: {t['symptoms']}
Patient History: {t['patient_history']}

Provide your response in plain text format. Your response should include:
1. Potential diagnoses (consider both the symptoms and patient history)
2. Recommended actions (e.g., seeking medical attention, lifestyle changes)
3. Any additional considerations for the patient

Format your response as follows:
Potential Diagnoses: [List of potential diagnoses]
Recommended Actions: [List of recommended actions]
Additional Considerations: [Any additional considerations for the patient]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include accurate potential diagnoses based on both the symptoms and patient history.",
            "The response should provide appropriate recommended actions.",
            "The response should consider the patient's history in the advice given.",
            "The response should be clear and ethically sound.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
