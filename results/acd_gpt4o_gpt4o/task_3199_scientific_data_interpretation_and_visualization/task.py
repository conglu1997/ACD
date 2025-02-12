class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"data": [[1, 2.3], [2, 3.5], [3, 5.1], [4, 7.2], [5, 9.4], [6, 11.8]], "description": "The data represents the growth of a bacterial culture over time. The first column is the time in hours, and the second column is the optical density (OD) measurements."},
            "2": {"data": [[0, 0], [10, 15], [20, 30], [30, 45], [40, 60], [50, 85]], "description": "The data represents the speed of a car over time. The first column is the time in seconds, and the second column is the speed in km/h."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the given scientific data and describe suitable visualizations for the data. Here is the data and its description:

Data: {t['data']}

Description: {t['description']}

1. Provide a summary of the data.
2. Describe at least one suitable visualization for the data, including the type of chart or graph, labels, and any other relevant details.
3. Explain why you chose the particular visualization(s).

Ensure that your visualizations are appropriate for the data and effectively communicate the information contained in the dataset. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The summary should accurately reflect the data provided.",
            "The described visualization should be suitable for the data.",
            "The description should include the type of chart or graph, labels, and other relevant details.",
            "The explanation should justify the choice of visualization(s)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
