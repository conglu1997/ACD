class TaskFamily:
    import json
    import statistics

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": [
                    {"description": "Temperature readings over a week in City A.", "values": [22, 24, 19, 21, 23, 20, 18]},
                    {"description": "Daily sales figures for Store B.", "values": [150, 200, 250, 180, 220, 190, 210]}
                ],
                "question": "What is the average temperature for City A, and how does it compare to the median daily sales figure for Store B?"
            },
            "2": {
                "data": [
                    {"description": "Student scores in Math during the semester.", "values": [85, 90, 78, 92, 88, 84, 76]},
                    {"description": "Attendance records for the same students.", "values": [90, 80, 85, 87, 88, 92, 85]}
                ],
                "question": "Calculate the average Math score and compare it to the average attendance record. What does this tell you about the relationship between attendance and performance?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        data_str = "\n".join([f"{d['description']}: {d['values']}" for d in t['data']])
        return f"""Your task is to interpret the following numerical data and textual descriptions to answer the question provided. Here is the data:
{data_str}

Question: {t['question']}

Provide your response in the following format:
- Average Temperature: [value]
- Median Sales Figure: [value]
- Comparison: [your comparison]

Ensure your comparison is clear and explains any observed relationships or differences between the numerical values."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        task_key = [k for k, v in TaskFamily.get_tasks().items() if v == t][0]
        def evaluate_task_1(submission: str) -> bool:
            correct_avg_temp = 21.0
            correct_median_sales = 200.0
            return f"- Average Temperature: {correct_avg_temp}" in submission and f"- Median Sales Figure: {correct_median_sales}" in submission
        def evaluate_task_2(submission: str) -> bool:
            correct_avg_score = round(sum([85, 90, 78, 92, 88, 84, 76]) / 7, 3)
            correct_avg_attendance = round(sum([90, 80, 85, 87, 88, 92, 85]) / 7, 3)
            return f"- Average Math Score: {correct_avg_score}" in submission and f"- Average Attendance Record: {correct_avg_attendance}" in submission
        if task_key == "1":
            return 1.0 if evaluate_task_1(submission) else 0.0
        elif task_key == "2":
            return 1.0 if evaluate_task_2(submission) else 0.0
        return 0.0
