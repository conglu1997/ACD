class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "analysis", "dataset": [[5, 12, 18, 20], [7, 14, 21, 25], [9, 18, 27, 30], [11, 22, 33, 35]], "context": "The dataset represents the growth of different plant species under controlled conditions over four weeks.", "task": "Analyze the given dataset and summarize the key observations."},
            "2": {"type": "conclusion", "dataset": [[2, 4, 8, 10], [3, 9, 27, 30], [4, 16, 64, 70], [5, 25, 125, 130]], "context": "The dataset represents the growth of bacterial cultures under different nutrient concentrations over a period of time.", "task": "Draw conclusions from the provided dataset about trends and patterns."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "analysis":
            return f"""Analyze the following dataset and summarize the key observations:\n\nContext: {t['context']}\nDataset: {t['dataset']}\n\nYour summary should include:\n1. Any noticeable patterns or trends.\n2. Insights about the relationships between the data points.\n3. Any outliers or anomalies present in the data.\n4. Possible implications of the observed patterns.\n\nSubmit your summary as a plain text string in the following format:\n\nSummary:\n[Your summary here]"""
        elif t["type"] == "conclusion":
            return f"""Draw conclusions from the following dataset about trends and patterns:\n\nContext: {t['context']}\nDataset: {t['dataset']}\n\nYour conclusions should include:\n1. Overall trends observed in the dataset.\n2. Any significant correlations between data points.\n3. Implications of the observed data trends.\n4. Any predictions or hypotheses based on the data.\n\nSubmit your conclusions as a plain text string in the following format:\n\nConclusions:\n[Your conclusions here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "analysis":
            criteria = ["The summary should include noticeable patterns or trends.", "The summary should provide insights about relationships between data points.", "The summary should identify any outliers or anomalies present in the data.", "The summary should discuss possible implications of the observed patterns."]
        elif t["type"] == "conclusion":
            criteria = ["The conclusions should include overall trends observed in the dataset.", "The conclusions should identify significant correlations between data points.", "The conclusions should discuss implications of the observed data trends.", "The conclusions should include any predictions or hypotheses based on the data."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
