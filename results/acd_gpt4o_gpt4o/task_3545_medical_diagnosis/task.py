class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"symptoms": "Patient presents with a persistent cough, shortness of breath, chest pain, and unexplained weight loss. History of smoking. Symptoms have lasted for over 3 weeks.", "patient_info": "45-year-old male, smoker for 20 years, no known allergies."},
            "2": {"symptoms": "Patient reports severe headache, fever, stiff neck, sensitivity to light, and a recent history of a rash. Symptoms started suddenly 24 hours ago.", "patient_info": "30-year-old female, no significant medical history."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to diagnose the fictional patient's condition based on the provided symptoms and patient information. Provide a thorough explanation of your reasoning, including possible conditions, necessary tests, and relevant medical knowledge.

Symptoms:
{t['symptoms']}

Patient Information:
{t['patient_info']}

Provide your diagnosis below. Your response should include:
1. The most likely diagnosis.
2. A detailed explanation of your reasoning.
3. Any additional tests or examinations you would recommend.
4. Consideration of differential diagnoses and why they were ruled out.

Format your response as follows:
Diagnosis: [Your diagnosis]
Reasoning: [Detailed explanation of your reasoning]
Additional Tests: [Any additional tests or examinations]
Differential Diagnoses: [Consideration of other potential conditions and why they were ruled out]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The diagnosis should be medically plausible.", "The reasoning should demonstrate an understanding of the symptoms and relevant medical knowledge.", "The response should include consideration of differential diagnoses.", "The additional tests or examinations should be appropriate for the symptoms provided."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
