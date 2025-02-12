class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"experiment": "photosynthesis", "parameters": "light intensity, carbon dioxide concentration"},
            "2": {"experiment": "pendulum motion", "parameters": "length of string, mass of bob"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["experiment"] == "photosynthesis":
            return f"""Your task is to simulate a scientific experiment on photosynthesis. Explain the steps you would take to measure the effect of different light intensities and carbon dioxide concentrations on the rate of photosynthesis. Predict the outcomes based on these parameters. Use scientific terminology where appropriate. Provide your response in the following format:\n\n1. Introduction: [Brief introduction to the experiment]\n2. Materials: [List of materials needed]\n3. Procedure: [Detailed steps of the experiment]\n4. Predictions: [Predicted outcomes based on the given parameters]\n"""
        elif t["experiment"] == "pendulum motion":
            return f"""Your task is to simulate a scientific experiment on pendulum motion. Explain the steps you would take to measure the effect of different lengths of string and masses of the bob on the period of the pendulum. Predict the outcomes based on these parameters. Use scientific terminology where appropriate. Provide your response in the following format:\n\n1. Introduction: [Brief introduction to the experiment]\n2. Materials: [List of materials needed]\n3. Procedure: [Detailed steps of the experiment]\n4. Predictions: [Predicted outcomes based on the given parameters]\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["experiment"] == "photosynthesis":
            criteria = ["The response should be formatted correctly.", "The procedure must be detailed and scientifically accurate.", "The predictions must be logical and based on the parameters given.", "The response should use scientific terminology appropriately."]
        elif t["experiment"] == "pendulum motion":
            criteria = ["The response should be formatted correctly.", "The procedure must be detailed and scientifically accurate.", "The predictions must be logical and based on the parameters given.", "The response should use scientific terminology appropriately."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
