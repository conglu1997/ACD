class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "patient_history": "A 45-year-old male presents with a persistent cough, shortness of breath, and chest pain. He has a history of smoking for 20 years, works in construction, and recently experienced weight loss and night sweats.",
                "symptoms": ["persistent cough", "shortness of breath", "chest pain", "weight loss", "night sweats"],
                "additional_info": "History of smoking for 20 years, works in construction"
            },
            "2": {
                "patient_history": "A 30-year-old female presents with fatigue, weight gain, cold intolerance, and hair loss. She has a family history of thyroid disorders and was recently diagnosed with anemia.",
                "symptoms": ["fatigue", "weight gain", "cold intolerance", "hair loss"],
                "additional_info": "Family history of thyroid disorders, recently diagnosed with anemia"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        symptoms_str = ', '.join(t['symptoms'])
        return f"""Diagnose the medical condition based on the following patient history and symptoms. Provide a detailed diagnosis and explain your reasoning. Here is the patient history:

{t['patient_history']}

Symptoms: {symptoms_str}

Additional information: {t['additional_info']}

Submit your diagnosis in the following format:

Diagnosis (be specific): [Your diagnosis here]
Reasoning: [Your detailed reasoning here]

Ensure your response is coherent and logically structured."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The diagnosis must be relevant to the symptoms and patient history.",
            "The reasoning must be clear, logical, and medically sound."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
