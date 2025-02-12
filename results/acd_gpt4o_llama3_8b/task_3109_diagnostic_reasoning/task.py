class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "context": "medical",
                "symptoms": ["fever", "dry cough", "shortness of breath", "loss of taste", "fatigue", "muscle pain"],
                "expected_diagnosis": "COVID-19"
            },
            "2": {
                "context": "technical",
                "issues": ["computer won't start", "black screen", "fan is running", "no beeps", "no power to peripherals (mouse, keyboard)", "power button unresponsive"],
                "expected_diagnosis": "power supply unit failure"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['context'] == 'medical':
            return f"""Based on the following medical symptoms, provide a diagnosis and explain your reasoning. Ensure that your explanation considers all the symptoms provided and mentions any differential diagnoses considered.

Symptoms: {', '.join(t['symptoms'])}

Submit your response as a plain text string in the following format:
Diagnosis: [Your diagnosis]
Explanation: [Your detailed explanation of how the symptoms lead to this diagnosis, including any relevant medical knowledge and differential diagnoses considered.]"""
        elif t['context'] == 'technical':
            return f"""Based on the following technical issues, provide a diagnosis and explain your reasoning. Ensure that your explanation considers all the issues provided and mentions any troubleshooting steps considered.

Issues: {', '.join(t['issues'])}

Submit your response as a plain text string in the following format:
Diagnosis: [Your diagnosis]
Explanation: [Your detailed explanation of how the issues lead to this diagnosis, including any relevant technical knowledge and troubleshooting steps considered.]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        expected_diagnosis = t['expected_diagnosis']
        validation_criteria = [f"The diagnosis should be '{expected_diagnosis}'.", "The explanation should consider all the provided symptoms or issues, be logically coherent, and include relevant domain-specific knowledge and differential diagnoses or troubleshooting steps."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
