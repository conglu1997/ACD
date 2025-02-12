import json

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": [
                    {"time": 0, "value": 10},
                    {"time": 1, "value": 12},
                    {"time": 2, "value": 15},
                    {"time": 3, "value": 18},
                    {"time": 4, "value": 22}
                ],
                "context": "A study observing the growth of a plant over time."
            },
            "2": {
                "data": [
                    {"temperature": 20, "activity": 5},
                    {"temperature": 25, "activity": 7},
                    {"temperature": 30, "activity": 8},
                    {"temperature": 35, "activity": 6},
                    {"temperature": 40, "activity": 4}
                ],
                "context": "An experiment measuring insect activity at different temperatures."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following tasks:

1. Analyze the given data set: {json.dumps(t['data'])}. Provide a detailed analysis that includes identifying patterns, trends, and any anomalies in the data.

2. Generate a scientific hypothesis based on the data and the provided context: {t['context']}. Ensure that your hypothesis is plausible, testable, and based on the observed data.

3. Evaluate your hypothesis by suggesting a potential experiment or study that could be conducted to test it. Describe the experimental setup, controls, and the type of data you would collect.

Submit your response as a plain text string in the following format:

Data Analysis:
[Your analysis]

Scientific Hypothesis:
[Your hypothesis]

Hypothesis Evaluation:
[Your evaluation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The data analysis should be detailed, accurate, and identify patterns, trends, and anomalies.",
            "The scientific hypothesis should be plausible, testable, and based on the observed data.",
            "The hypothesis evaluation should suggest a well-defined experiment, including controls and types of data to be collected.",
            "The submission should be well-organized and clearly written."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
