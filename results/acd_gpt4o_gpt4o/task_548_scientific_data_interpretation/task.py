class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": "Temperature (C): [20, 22, 24, 26, 28, 30]\nGrowth Rate (cm/day): [0.5, 0.6, 0.8, 1.0, 1.1, 1.3]",
                "context": "A researcher is studying the effect of temperature on the growth rate of a particular plant species."
            },
            "2": {
                "data": "Light Intensity (lux): [100, 200, 400, 600, 800, 1000]\nPhotosynthesis Rate (umol/m^2/s): [2, 3, 4.5, 5, 5.5, 6]",
                "context": "A researcher is studying the effect of light intensity on the rate of photosynthesis in a specific plant species."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the given scientific data and generate a hypothesis based on the observations. Use the provided context to help guide your hypothesis generation.\n\nContext: {t["context"]}\n\nData:\n{t["data"]}\n\nYour response should include:\n1. A clear and concise hypothesis based on the data.\n2. A brief explanation of how the data supports your hypothesis.\n\nEnsure your response is well-structured and demonstrates a deep understanding of the data."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
