class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "dataset": [
                    {"age": 23, "income": 50000, "education": "bachelor"},
                    {"age": 45, "income": 80000, "education": "master"},
                    {"age": 34, "income": 75000, "education": "phd"},
                    {"age": 29, "income": 62000, "education": "bachelor"},
                    {"age": 41, "income": 70000, "education": "master"},
                    {"age": 38, "income": 72000, "education": "phd"},
                    {"age": 26, "income": 54000, "education": "bachelor"},
                    {"age": 52, "income": 90000, "education": "master"},
                    {"age": 47, "income": 85000, "education": "phd"},
                    {"age": 31, "income": 60000, "education": "bachelor"},
                    {"age": 44, "income": 82000, "education": "master"},
                    {"age": 36, "income": 77000, "education": "phd"},
                    {"age": 28, "income": 61000, "education": "bachelor"},
                    {"age": 39, "income": 73000, "education": "master"},
                    {"age": 50, "income": 88000, "education": "phd"}
                ],
                "analysis_type": "mean_income_by_education"
            },
            "2": {
                "dataset": [
                    {"height": 5.5, "weight": 150},
                    {"height": 6.2, "weight": 180},
                    {"height": 5.8, "weight": 165},
                    {"height": 6.0, "weight": 170},
                    {"height": 5.6, "weight": 155},
                    {"height": 5.9, "weight": 160},
                    {"height": 6.1, "weight": 175},
                    {"height": 5.7, "weight": 158},
                    {"height": 6.3, "weight": 185},
                    {"height": 5.4, "weight": 145},
                    {"height": 5.3, "weight": 140},
                    {"height": 6.4, "weight": 190},
                    {"height": 5.1, "weight": 135},
                    {"height": 6.5, "weight": 195},
                    {"height": 5.2, "weight": 138}
                ],
                "analysis_type": "correlation_height_weight"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        analysis_type = t["analysis_type"]
        dataset = t["dataset"]
        instructions = f"""Your task is to perform a statistical analysis on the given dataset and explain the results.

Dataset: {dataset}

Analysis Type: {analysis_type}

For 'mean_income_by_education', calculate the mean income for each education level and provide a summary of your findings.
For 'correlation_height_weight', calculate the correlation coefficient between height and weight and explain what it signifies.

Ensure your analysis is accurate and your explanation is clear and concise. Provide your response in plain text format with the following structure:

1. Analysis Method: [Describe your analysis method]
2. Results: [Present your results]
3. Explanation: [Explain what the results signify]
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The statistical analysis should be accurate.",
            "The explanation of the results should be clear and concise.",
            "For mean_income_by_education: The mean income for each education level should be correctly calculated and summarized.",
            "For correlation_height_weight: The correlation coefficient should be correctly calculated and its significance should be accurately explained."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
