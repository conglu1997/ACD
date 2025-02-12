class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "phenomenon": "Photosynthesis",
                "data": "During an experiment, it was observed that plants exposed to red light grew faster than those exposed to green light."
            },
            "2": {
                "phenomenon": "Newton's Third Law of Motion",
                "data": "In a vacuum, two objects of different masses fall at the same rate regardless of their mass."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Explain the following scientific phenomenon and generate a hypothesis based on the provided data or observations:

Phenomenon: {t['phenomenon']}

Data/Observation: {t['data']}

Your explanation should be clear and comprehensive, covering the key principles behind the phenomenon. Then, generate a plausible hypothesis that could explain the provided data or observations. Ensure your hypothesis is logically consistent with the data and can be tested experimentally. Logical coherence and experimental testability are crucial. Submit your explanation and hypothesis as a plain text string in the following format:

Explanation:
[Your explanation]

Hypothesis:
[Your hypothesis]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The explanation should clearly cover the key principles behind the phenomenon.", "The hypothesis should be logically consistent with the provided data or observations.", "The hypothesis should be testable experimentally."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
