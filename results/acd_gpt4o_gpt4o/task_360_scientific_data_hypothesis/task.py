class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"dataset": "Temperature (°C), Humidity (%), Plant Growth (cm)\n20, 30, 5\n25, 40, 6\n30, 50, 10\n35, 60, 14\n40, 70, 13", "description": "This dataset shows the relationship between temperature, humidity, and plant growth in a controlled environment."},
            "2": {"dataset": "Age, Exercise (hours/week), Health Score\n20, 5, 80\n30, 4, 78\n40, 3, 72\n50, 2, 68\n60, 1, 65", "description": "This dataset shows the relationship between age, weekly exercise hours, and health scores."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the following dataset and generate plausible scientific hypotheses or explanations based on the data.\n\nDataset Description: {t['description']}\n\nDataset:\n{t['dataset']}\n\nYour response should include:\n1. A clear and concise hypothesis or explanation that is logically derived from the data.\n2. A brief rationale explaining how you arrived at this hypothesis based on the data provided.\n\nEnsure your hypothesis is scientifically plausible and well-supported by the data. Format your response in plain text without any additional formatting."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a clear and concise hypothesis or explanation that is logically derived from the data.",
            "The response should include a brief rationale explaining how the hypothesis was derived from the data.",
            "The hypothesis should be scientifically plausible and well-supported by the data."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
