class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'criteria': 'Describe the events leading up to and including the signing of the Declaration of Independence in 1776. Ensure to include key figures, dates, and the outcome of the event.'},
            '2': {'criteria': 'Describe the events and significance of the fall of the Berlin Wall in 1989. Ensure to include key figures, dates, and the outcome of the event.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Generate a detailed description of the historical event based on the following criteria: {t['criteria']}\nStructure your description into clear sections, detailing the key figures, dates, and outcomes. Ensure that your description is comprehensive, historically accurate, and logically consistent. Submit your description as a plain text string in the following format:\n\n1. Key Figures: [Your description]\n2. Dates: [Your description]\n3. Outcomes: [Your description]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should accurately reflect the given criteria.", "The description should be detailed, historically accurate, and logically structured.", "The description should logically explain the sequence of events and their significance.", "The response should follow the given format and cover all specified sections.", "The description should be coherent and maintain a logical flow."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
