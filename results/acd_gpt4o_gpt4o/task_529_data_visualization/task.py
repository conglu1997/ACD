import matplotlib.pyplot as plt
import pandas as pd
import io

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": "Year,Sales\n2015,150\n2016,200\n2017,250\n2018,300\n2019,350\n2020,400\n",
                "question": "Generate a line plot to visualize the sales data over the years."},
            "2": {
                "data": "Product,Revenue\nA,5000\nB,7000\nC,8000\nD,6500\nE,7200\n",
                "question": "Generate a bar chart to compare the revenue of different products."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a data visualization based on the provided dataset and question.

Dataset:
{t['data']}

Question:
{t['question']}

Ensure your visualization accurately represents the data and addresses the given question. Submit your response as a Python code snippet that can be executed to generate the requested plot."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The submission should generate the correct type of plot as requested.",
                   "The plot should accurately represent the data provided in the dataset.",
                   "The plot should be clear, correctly labeled, and easy to interpret."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
