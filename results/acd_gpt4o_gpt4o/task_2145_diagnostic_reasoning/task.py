class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"context": "medical", "symptoms": "fever, headache, neck stiffness, sensitivity to light, nausea, confusion"},
            "2": {"context": "technical", "symptoms": "computer won't start, power light is off, no fan noise, occasional beeping sound, recent storm"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['context'] == 'medical':
            return f"""Your task is to diagnose the medical condition based on the given symptoms and provide a rationale for your diagnosis.

Symptoms: {t['symptoms']}

Instructions:
1. Diagnose the most likely medical condition based on the symptoms.
2. Provide a detailed rationale explaining why you arrived at this diagnosis.
3. Ensure that your diagnosis and rationale are coherent and logically sound.

Your response should be in the following format:
Diagnosis: [Your diagnosis]
Rationale: [Your rationale]"""
        elif t['context'] == 'technical':
            return f"""Your task is to diagnose the technical problem based on the given symptoms and provide a rationale for your diagnosis.

Symptoms: {t['symptoms']}

Instructions:
1. Diagnose the most likely technical problem based on the symptoms.
2. Provide a detailed rationale explaining why you arrived at this diagnosis.
3. Ensure that your diagnosis and rationale are coherent and logically sound.

Your response should be in the following format:
Diagnosis: [Your diagnosis]
Rationale: [Your rationale]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['context'] == 'medical':
            criteria = ["The diagnosis should be a plausible medical condition based on the symptoms.", "The rationale should explain why the symptoms lead to the diagnosis."]
        elif t['context'] == 'technical':
            criteria = ["The diagnosis should be a plausible technical issue based on the symptoms.", "The rationale should explain why the symptoms lead to the diagnosis."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
