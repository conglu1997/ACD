class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "sequence": ["sunrise", "morning", "afternoon", "evening", "night", "midnight", "early morning"],
                "criteria": "Predict the next event in the sequence after 'early morning'."
            },
            "2": {
                "sequence": ["seed", "sprout", "plant", "flower", "fruit", "decay", "soil"],
                "criteria": "Predict the next event in the sequence after 'soil'."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Predict the next event in the given temporal sequence based on the provided pattern.

Sequence: {t['sequence']}
Criteria: {t['criteria']}

Your response should include:
1. An explanation of the sequence pattern and your reasoning for the prediction.
2. The predicted next event based on the given criteria.

Example response format:
- Explanation: The sequence follows a daily cycle from sunrise to early morning. After early morning, the cycle repeats, so the next event is sunrise.
- Prediction: sunrise

Ensure your explanation is clear and logically consistent, and your prediction accurately follows the identified pattern. Submit your response as a plain text string in the following format:
- Explanation: [Your explanation here]
- Prediction: [Your prediction here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should clearly describe the identified pattern in the sequence.",
            "The prediction should logically follow from the described pattern.",
            "The response should follow the specified format precisely."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
