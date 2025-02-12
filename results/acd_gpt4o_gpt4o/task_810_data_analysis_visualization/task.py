class TaskFamily:
    import pandas as pd
    import matplotlib.pyplot as plt
    from io import StringIO

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": "A,B,C\n1,2,3\n4,5,6\n7,8,9\n",
                "description": "Interpret the given dataset and create a bar chart showing the sum of each column."
            },
            "2": {
                "data": "Category,Value\nA,10\nB,20\nC,30\nD,40\n",
                "description": "Interpret the given dataset and create a pie chart showing the distribution of values across categories."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        data = t["data"]
        description = t["description"]
        instructions = f"""Your task is to interpret the given dataset and create a visual representation based on the following description:\n\nDescription:\n{description}\n\nDataset:\n{data}\n\nEnsure that your visualization is accurate, clear, and effectively conveys the insights from the data. Provide your submission in plain text format with the visualization code and a brief explanation of the insights. Example format:\n\nCode:\n[Your visualization code]\n\nExplanation:\n[Your explanation]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The visualization should accurately represent the data.",
            "The explanation should clearly convey the insights from the data."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
