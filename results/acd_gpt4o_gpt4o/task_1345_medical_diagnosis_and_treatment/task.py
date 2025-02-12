class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"symptoms": "Patient presents with a persistent cough, shortness of breath, and chest pain. Symptoms have been ongoing for 3 weeks. Patient has a history of smoking."},
            "2": {"symptoms": "Patient presents with severe headache, fever, neck stiffness, and sensitivity to light. Symptoms started suddenly 2 days ago. Patient has no significant medical history."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to diagnose the medical condition based on the following symptoms and provide a detailed treatment plan.

Symptoms: {t['symptoms']}

Your response should include:
1. The most likely diagnosis.
2. A brief explanation of how you arrived at this diagnosis.
3. A detailed treatment plan that addresses the diagnosis.

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a clear and accurate diagnosis.",
            "The explanation should logically connect the symptoms to the diagnosis.",
            "The treatment plan should be appropriate and detailed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
