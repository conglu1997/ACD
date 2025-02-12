class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"data": [
                {"time": 0, "temperature": 20},
                {"time": 1, "temperature": 22},
                {"time": 2, "temperature": 24},
                {"time": 3, "temperature": 23},
                {"time": 4, "temperature": 21},
                {"time": 5, "temperature": 19},
                {"time": 6, "temperature": 18},
                {"time": 7, "temperature": 20},
                {"time": 8, "temperature": 21},
                {"time": 9, "temperature": 22},
                {"time": 10, "temperature": 23},
                {"time": 11, "temperature": 25},
                {"time": 12, "temperature": 27},
                {"time": 13, "temperature": 26},
                {"time": 14, "temperature": 24},
                {"time": 15, "temperature": 23},
                {"time": 16, "temperature": 22}
            ], "question": "What is the average temperature over the given time period? Provide your answer rounded to one decimal place."},
            "2": {"data": [
                {"day": 1, "growth": 2.1},
                {"day": 2, "growth": 2.4},
                {"day": 3, "growth": 3.0},
                {"day": 4, "growth": 3.5},
                {"day": 5, "growth": 4.0},
                {"day": 6, "growth": 4.4},
                {"day": 7, "growth": 4.8},
                {"day": 8, "growth": 5.1},
                {"day": 9, "growth": 5.3},
                {"day": 10, "growth": 5.6},
                {"day": 11, "growth": 5.8},
                {"day": 12, "growth": 6.0},
                {"day": 13, "growth": 6.2},
                {"day": 14, "growth": 6.3}
            ], "question": "Based on the data, what is the projected growth on day 18? Provide your answer rounded to one decimal place."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to analyze the following scientific data and answer the specified question:

Data: {t['data']}

Question: {t['question']}

Provide your answer in plain text format with a clear explanation of how you arrived at the conclusion. Format your response as follows:
Answer: <your answer>
Explanation: <your explanation>"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The answer should be accurate based on the data provided.",
            "The answer should include a clear explanation of how the conclusion was reached.",
            "The answer should be in the correct format: plain text and numerical values rounded to one decimal place."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
