class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "advice", "profession": "Software Developer", "scenario": "A mid-level developer wants to transition into a project management role."},
            "2": {"task_type": "advice", "profession": "Graphic Designer", "scenario": "A graphic designer wants to specialize in UX/UI design."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to provide detailed and contextually appropriate career advice for the following scenario:\n\nProfession: {t['profession']}\nScenario: {t['scenario']}\n\nEnsure your advice includes:\n1. Key steps to transition or advance in the career.\n2. Relevant skills or qualifications needed.\n3. Potential challenges and how to overcome them.\n4. Any additional tips for success.\n\nProvide your response in plain text format, structured as follows:\n\nAdvice: [Your detailed career advice]\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should be formatted as 'Advice: [Your detailed career advice]'.", "The advice must be relevant to the given profession and scenario.", "The advice must include key steps, relevant skills, potential challenges, and additional tips."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
