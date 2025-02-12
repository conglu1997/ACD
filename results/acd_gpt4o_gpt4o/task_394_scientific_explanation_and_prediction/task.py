class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"phenomenon": "Explain how photosynthesis works and predict the impact on plant growth if the light intensity is reduced by half.", "data": "Light intensity reduced by 50%. Consider the effects on chlorophyll absorption and overall plant growth."},
            "2": {"phenomenon": "Describe the greenhouse effect and predict the impact on global temperatures if the concentration of CO2 in the atmosphere doubles.", "data": "CO2 concentration doubled. Account for the effect on thermal radiation and heat retention in the atmosphere."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to explain the following scientific phenomenon and make a prediction based on the given scientific data:

Phenomenon: {t['phenomenon']}

Data: {t['data']}

Ensure that your explanation is clear, detailed, and scientifically accurate. Your prediction should be logical and based on the data provided. Provide your response in plain text format with the following structure:

1. Explanation of the phenomenon
2. Prediction based on the data

Be sure to address the key scientific concepts and reasoning behind your predictions."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should be scientifically accurate.", "The prediction should logically follow from the provided data.", "The response should be clear and detailed.", "The response should address key scientific concepts and reasoning."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
