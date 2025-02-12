class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        # Sample datasets for analysis
        dataset1 = '''date,value
2023-01-01,100
2023-01-02,110
2023-01-03,120
2023-01-04,130
2023-01-05,140
2023-01-06,150
2023-01-07,160
2023-01-08,170
2023-01-09,180
2023-01-10,190
2023-01-11,200
2023-01-12,210
2023-01-13,220
2023-01-14,230
2023-01-15,240
2023-01-16,250
2023-01-17,260
2023-01-18,270
2023-01-19,280
2023-01-20,290
2023-01-21,300
2023-01-22,310
2023-01-23,320
2023-01-24,330
2023-01-25,340
2023-01-26,350
2023-01-27,360
2023-01-28,370
2023-01-29,380
2023-01-30,390
2023-01-31,400
'''
        dataset2 = '''date,temperature
2023-07-01,30
2023-07-02,32
2023-07-03,31
2023-07-04,29
2023-07-05,28
2023-07-06,30
2023-07-07,31
2023-07-08,33
2023-07-09,34
2023-07-10,32
2023-07-11,35
2023-07-12,36
2023-07-13,34
2023-07-14,33
2023-07-15,32
2023-07-16,31
2023-07-17,30
2023-07-18,29
2023-07-19,28
2023-07-20,27
2023-07-21,26
2023-07-22,25
2023-07-23,24
2023-07-24,23
2023-07-25,22
2023-07-26,21
2023-07-27,20
2023-07-28,19
2023-07-29,18
2023-07-30,17
2023-07-31,16
'''
        return {
            "1": {"dataset": dataset1, "task": "Analyze the time series data and provide a summary of trends, patterns, and potential future values."},
            "2": {"dataset": dataset2, "task": "Analyze the temperature data and summarize the key insights and possible future temperature trends."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are provided with the following dataset:

{t['dataset']}

Task: {t['task']}

Your response should include:
1. A summary of the trends or patterns observed in the data, including any notable fluctuations or anomalies.
2. Predictions or potential future values based on the analysis, including reasoning behind these predictions.
3. Clear and concise explanations of the insights derived from the data analysis, detailing any observed correlations or causations.

Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should include a summary of the trends or patterns observed in the data, including notable fluctuations or anomalies.",
            "The response should include predictions or potential future values with reasoning.",
            "The explanations should be clear, concise, and detail observed correlations or causations."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
