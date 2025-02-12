class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": "Temperature (°C): [10, 20, 30, 40, 50]\nGrowth Rate (cm/day): [2, 4, 6, 8, 10]",
                "criteria": "Interpret the given data and generate a hypothesis about the relationship between temperature and growth rate. Design an experiment to test your hypothesis."
            },
            "2": {
                "data": "Fertilizer Type: [A, B, C, D]\nPlant Height (cm): [15, 20, 25, 30]",
                "criteria": "Interpret the given data and generate a hypothesis about the effect of different fertilizer types on plant height. Design an experiment to test your hypothesis."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the following scientific data, generate a hypothesis, and design an experiment to test your hypothesis.

Data: {t['data']}

Criteria: {t['criteria']}

For both tasks, provide your hypothesis in plain text format and outline the experimental design, including the variables, control groups, and methods. Ensure your explanation is clear, logical, and scientifically sound."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The hypothesis should be a logical interpretation of the given data.",
            "The experimental design should include clear variables, control groups, and methods.",
            "The explanation should be scientifically sound and logically structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
