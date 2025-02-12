class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "dataset": [
                    {"age": 23, "income": 45000, "education": "Bachelor's"},
                    {"age": 45, "income": 85000, "education": "Master's"},
                    {"age": 36, "income": 60000, "education": "Bachelor's"},
                    {"age": 29, "income": 50000, "education": "PhD"},
                    {"age": 50, "income": 90000, "education": "Master's"},
                    {"age": 40, "income": 70000, "education": "Bachelor's"},
                    {"age": 28, "income": 48000, "education": "Bachelor's"},
                    {"age": 55, "income": 95000, "education": "PhD"},
                    {"age": 60, "income": 100000, "education": "Master's"},
                    {"age": 33, "income": 52000, "education": "Bachelor's"},
                    {"age": 37, "income": 62000, "education": "Master's"},
                    {"age": 42, "income": 78000, "education": "PhD"},
                    {"age": 31, "income": 56000, "education": "Bachelor's"}
                ],
                "task": "Analyze the dataset to identify any trends or insights related to age, income, and education level. Provide a summary of your findings, including any relevant statistical analysis (e.g., mean, median, correlation)."
            },
            "2": {
                "dataset": [
                    {"temperature": 70, "humidity": 45, "wind_speed": 12},
                    {"temperature": 75, "humidity": 50, "wind_speed": 15},
                    {"temperature": 80, "humidity": 55, "wind_speed": 10},
                    {"temperature": 85, "humidity": 60, "wind_speed": 8},
                    {"temperature": 90, "humidity": 65, "wind_speed": 5},
                    {"temperature": 95, "humidity": 70, "wind_speed": 3},
                    {"temperature": 100, "humidity": 75, "wind_speed": 2},
                    {"temperature": 105, "humidity": 80, "wind_speed": 1},
                    {"temperature": 110, "humidity": 85, "wind_speed": 0},
                    {"temperature": 115, "humidity": 90, "wind_speed": 0},
                    {"temperature": 120, "humidity": 95, "wind_speed": 0},
                    {"temperature": 125, "humidity": 100, "wind_speed": 0},
                    {"temperature": 130, "humidity": 105, "wind_speed": 0}
                ],
                "task": "Analyze the dataset to identify any trends or insights related to temperature, humidity, and wind speed. Provide a summary of your findings, including any relevant statistical analysis (e.g., mean, median, correlation)."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are required to analyze the given dataset and provide a summary of your findings. Your analysis should include the following statistical measures: mean, median, and correlation. Additionally, identify any insights or trends you can derive from the statistical measures.

Dataset: {t['dataset']}

Task: {t['task']}

Submit your response as a plain text string in the following format:

1. Statistical Measures: [List the statistical measures you calculated (e.g., means, medians, correlations) and their values]
2. Trends/Insights: [Describe the trends or insights you identified in the dataset based on your analysis. Ensure that your insights are derived from the statistical measures calculated.]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The analysis should include relevant statistical measures (mean, median, correlation).",
            "The summary should identify any trends or insights based on the dataset.",
            "The response should be coherent and logically organized.",
            "The insights should be derived from the statistical measures calculated."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
