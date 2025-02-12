class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "dataset": "Year, Sales\n2015, 200\n2016, 300\n2017, 400\n2018, 500\n2019, 600\n2020, 700\n2021, 650\n2022, 800",
                "visualization_type": "line chart"
            },
            "2": {
                "dataset": "Category, Count\nA, 10\nB, 15\nC, 5\nD, 20\nE, 25",
                "visualization_type": "bar chart"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a {t['visualization_type']} based on the following dataset and then provide a brief explanation of the visualization. The dataset is:\n\n{t['dataset']}\n\nSubmit your visualization as a description of the plot and your explanation in plain text format. Make sure to include key elements such as axis labels, data points, and any noticeable trends in your description."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The visualization description should accurately represent the given dataset, including key elements such as axis labels, data points, and trends.", "The explanation should clearly interpret the data shown in the visualization.", "The submission should be clear and written in proper English."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
