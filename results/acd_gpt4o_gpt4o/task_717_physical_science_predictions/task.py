class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A ball is dropped from a height of 10 meters on Earth. Describe what happens to the ball, considering air resistance and energy transformations. Predict its behavior over time, including any rebounds.", "task_type": "prediction"},
            "2": {"scenario": "Explain why a helium balloon rises in the air, considering the concepts of buoyancy, density, and pressure. Include a discussion on how different conditions (e.g., temperature) might affect this behavior.", "task_type": "explanation"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "prediction":
            return """Your task is to predict the outcome of the following physical science scenario:

{0}

Ensure that your prediction is based on sound scientific principles and includes a clear, detailed explanation of the physical processes involved. Provide your response in plain text format, including any relevant equations or calculations.""".format(t["scenario"])
        elif t["task_type"] == "explanation":
            return """Your task is to explain the phenomenon described in the following scenario:

{0}

Ensure that your explanation is based on sound scientific principles and includes a clear, detailed description of the physical processes involved. Provide your response in plain text format, including any relevant equations or calculations where applicable.""".format(t["scenario"])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The prediction should be scientifically accurate, considering factors like air resistance, energy transformations, and should include relevant equations or calculations." if t["task_type"] == "prediction" else "The explanation should accurately describe the physical processes involved, considering factors like buoyancy, density, pressure, and should include relevant equations or calculations where applicable."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
