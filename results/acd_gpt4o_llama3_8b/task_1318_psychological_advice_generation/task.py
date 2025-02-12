class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A person named Alex is feeling overwhelmed with work and personal responsibilities. They are finding it hard to balance their time and feel constantly stressed. What advice would you give Alex to help them manage their stress and improve their work-life balance?"
            },
            "2": {
                "scenario": "Jordan has recently gone through a breakup and is struggling with feelings of loneliness and sadness. They feel like they will never find happiness again. What advice would you give Jordan to help them cope with their feelings and start moving forward?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Read the following emotional scenario and provide appropriate psychological advice:

Scenario:
{t['scenario']}

Ensure your advice is empathetic, practical, and supportive. Submit your response as a plain text string in the following format:

Advice: [Your advice]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The advice should be empathetic and supportive.", "The advice should be practical and actionable.", "The advice should help the individual manage their emotions and improve their situation."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
