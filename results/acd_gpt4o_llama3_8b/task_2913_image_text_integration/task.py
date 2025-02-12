class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "image_description": "A bar chart showing sales data for three products (A, B, C) over four quarters. The chart shows that Product A has steadily increased each quarter, Product B has fluctuated with a peak in Q2 and a dip in Q3, and Product C has remained relatively stable with a slight increase in Q4.",
                "text_data": "Based on the sales data provided in the bar chart, determine which product had the highest average sales across all quarters and explain why."
            },
            "2": {
                "image_description": "A line graph depicting the temperature changes over a week in three cities (X, Y, Z). City X shows a gradual increase in temperature, City Y shows a sharp rise followed by a gradual decline, and City Z shows a consistent temperature with minor fluctuations.",
                "text_data": "Using the temperature data from the line graph, identify which city had the most stable temperature over the week and justify your choice."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are provided with a description of a chart and some textual data. Your task is to interpret the chart based on its description and use this information to answer a question or solve a problem. Ensure your response is clear and uses information from both the image description and the text data.

Image Description: {t['image_description']}
Text Data: {t['text_data']}

Submit your response in the following format:
1. Answer: [Your answer]
2. Explanation: [Your detailed explanation using both the image description and the text data]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The answer should correctly identify the required information based on the chart description.",
            "The explanation should clearly use details from both the image description and the text data.",
            "The response should be coherent and logically structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
