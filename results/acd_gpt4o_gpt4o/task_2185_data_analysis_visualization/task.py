class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "analyze", "dataset": [["Year", "Sales"], [2016, 120], [2017, 130], [2018, 150], [2019, 200], [2020, 250], [2021, 300], [2022, 280]], "question": "What are the key trends in the sales data over the years?"},
            "2": {"task_type": "visualize", "dataset": [["Month", "Revenue"], ["January", 5000], ["February", 4800], ["March", 5300], ["April", 6000], ["May", 6200], ["June", 6100]], "instruction": "Create a bar chart to visualize the revenue data for each month."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "analyze":
            instructions = f"""Your task is to analyze the following dataset and answer the question based on the data provided:

Dataset: {t['dataset']}

Question: {t['question']}

Provide your analysis in plain text format. Ensure your response is well-structured, logical, and addresses the key trends or insights from the data."""
        else:
            instructions = f"""Your task is to create a bar chart based on the provided dataset. Ensure that the bar chart is clear, accurate, and effectively visualizes the data.

Dataset: {t['dataset']}

Instruction: {t['instruction']}

Provide your visualization in plain text format, using a common text-based representation for bar charts. For example:

January: ##### (5000)
February: #### (4800)
March: ###### (5300)
April: ####### (6000)
May: ######## (6200)
June: ####### (6100)"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "analyze":
            criteria = ["The response should correctly identify key trends in the data and provide logical insights without any inaccuracies."]
        else:
            criteria = ["The visualization should accurately represent the data and be clear and easy to understand."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
