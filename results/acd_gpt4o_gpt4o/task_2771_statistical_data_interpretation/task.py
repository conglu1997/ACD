class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "interpret", "data": "{\"mean\": 20, \"median\": 18, \"mode\": 17, \"std_dev\": 4}"},
            "2": {"task_type": "generate", "data": [23, 19, 21, 25, 18, 20, 22, 24, 19, 21]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'interpret':
            return f"""Your task is to interpret the following statistical data and provide a detailed summary of its implications.

Data: {t['data']}

Instructions:
1. Provide a comprehensive summary of the given statistical data.
2. Explain what the mean, median, mode, and standard deviation indicate about the data set.
3. Ensure your summary is clear and insightful.

Your response should be in the following format:
Summary: [Your summary]"""
        elif t['task_type'] == 'generate':
            return f"""Your task is to generate a detailed statistical summary based on the given data set.

Data Set: {t['data']}

Instructions:
1. Calculate the mean, median, mode, and standard deviation for the provided data set.
2. Provide a detailed summary that includes these statistical measures.
3. Ensure your summary is clear and accurate.

Your response should be in the following format:
Summary: [Your summary]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'interpret':
            criteria = ["The summary should be comprehensive and insightful.", "The summary should accurately explain what the mean, median, mode, and standard deviation indicate about the data set."]
        elif t['task_type'] == 'generate':
            criteria = ["The summary should accurately calculate and include the mean, median, mode, and standard deviation.", "The summary should be clear and accurate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
