class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "phenomenon": "Photosynthesis",
                "data": "A plant is placed in a sealed transparent container with a light source and water. Predict the changes in oxygen and carbon dioxide levels over a period of 24 hours, assuming the plant is healthy and actively photosynthesizing."
            },
            "2": {
                "phenomenon": "Newton's Third Law",
                "data": "A rocket is launched in a vacuum. Predict the motion of the rocket and the expulsion of gases over the first 10 seconds of flight, assuming constant thrust."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        phenomenon = t['phenomenon']
        data = t['data']
        return f"""Explain the scientific phenomenon: {phenomenon}. Based on the following data, predict the outcomes:

{data}

Your response should include:
1. A detailed explanation of the phenomenon, including the underlying scientific principles.
2. A prediction of the outcomes based on the provided data, clearly linking the explanation to the prediction.

Submit your response as a plain text string in the following format:

Explanation: [Your explanation]
Prediction: [Your prediction]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should accurately describe the scientific phenomenon, including the underlying principles.",
            "The prediction should logically follow from the data provided and the explanation of the phenomenon, clearly linking the two."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
