class TaskFamily:
    import random
    
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'task': 'How to change a flat tire on a car, including the use of a jack and lug wrench.'},
            '2': {'task': 'How to bake a basic loaf of bread, including kneading the dough and proofing.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate clear, step-by-step instructions for the following task:
Task: {t['task']}

Your instructions should be detailed and easy to follow. Each step should be clear and concise, ensuring that someone without prior experience can complete the task successfully. Submit your instructions as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The instructions should be clear and easy to follow.',
            'Each step should be detailed and concise.',
            'The instructions should cover all necessary steps to complete the task successfully.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
