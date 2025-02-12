class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "symptoms": "A 45-year-old male presents with a persistent cough, shortness of breath, and chest pain. He also has a history of smoking."
            },
            "2": {
                "symptoms": "A 30-year-old female presents with severe headache, fever, neck stiffness, and sensitivity to light."
            },
            "3": {
                "symptoms": "A 60-year-old female presents with fatigue, weight gain, dry skin, and sensitivity to cold."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a plausible medical diagnosis based on the following symptoms:

Symptoms: {t['symptoms']}

Your diagnosis should be relevant to the symptoms provided and should include a brief explanation. Submit your diagnosis as a plain text string in the format 'Diagnosis: [Your diagnosis]. Explanation: [Your explanation].'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The diagnosis should be relevant to the symptoms provided.",
            "The diagnosis should include a brief explanation."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
