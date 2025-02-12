class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "dilemma": "A doctor has a single dose of a life-saving medication but two patients who need it equally. One patient is a young child, and the other is an elderly person with significant contributions to society."
            },
            "2": {
                "dilemma": "An autonomous car must decide between swerving to avoid hitting a group of pedestrians, which would result in the car crashing and potentially harming its passenger, or continuing its path and harming the pedestrians."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a detailed scenario for the following ethical dilemma. Include the perspectives of different stakeholders involved (e.g., the people directly affected, their families, and society). Ensure the scenario is coherent, plausible, and empathetic.

Dilemma:
{t['dilemma']}

Submit your scenario as a plain text string in the following format:
'Scenario: [Your detailed scenario]'
'Stakeholder Perspectives: [Different perspectives]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The scenario must be coherent and plausible.", "The scenario must include the perspectives of different stakeholders.", "The scenario must demonstrate empathy."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
