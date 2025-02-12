class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "symptoms": "A 45-year-old male experiencing severe chest pain, shortness of breath, and sweating. The pain radiates to the left arm and jaw.",
                "patient_history": "No known history of heart disease, but a family history of cardiovascular issues, and the patient is a smoker."
            },
            "2": {
                "symptoms": "A 30-year-old female with persistent, throbbing headaches, nausea, and sensitivity to light and sound. The headaches occur several times a month and last for hours.",
                "patient_history": "History of migraines, high-stress job, and irregular sleep patterns."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the provided symptoms and patient history, provide medical advice. Ensure your advice includes:
1. Potential diagnoses.
2. Recommended actions.
3. Necessary follow-up or lifestyle changes.

Your response should be clear, accurate, and relevant to the given symptoms and patient history. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The advice should be medically accurate and relevant to the symptoms and patient history.",
            "The response should include potential diagnoses.",
            "The response should include recommended actions.",
            "The response should include necessary follow-up or lifestyle changes."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
