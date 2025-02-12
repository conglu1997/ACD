class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"experiment": "pendulum", "length": 2, "mass": 1, "angle": 30, "instructions": "Explain the principle of a simple pendulum and predict the period of oscillation given a pendulum of length 2 meters, mass 1 kg, and an initial angle of 30 degrees."},
            "2": {"experiment": "free_fall", "height": 10, "mass": 0.5, "instructions": "Explain the principle of free fall and predict the time it takes for an object of mass 0.5 kg to fall from a height of 10 meters."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["experiment"] == "pendulum":
            return f"Your task is to explain the principle behind a simple pendulum and predict the period of oscillation given the following conditions: length of the pendulum is {t['length']} meters, mass is {t['mass']} kg, and initial angle is {t['angle']} degrees. Ensure your explanation covers the relevant physics concepts and your prediction is numerically accurate based on these conditions. Provide your response in plain text format, structured as follows:\n1. Explanation of the principle\n2. Prediction of the period of oscillation\nNote: Both parts are required for a successful score."
        elif t["experiment"] == "free_fall":
            return f"Your task is to explain the principle behind free fall and predict the time it takes for an object to fall from a height of {t['height']} meters given a mass of {t['mass']} kg. Ensure your explanation covers the relevant physics concepts and your prediction is numerically accurate based on these conditions. Provide your response in plain text format, structured as follows:\n1. Explanation of the principle\n2. Prediction of the time to fall\nNote: Both parts are required for a successful score."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["experiment"] == "pendulum":
            criteria = [
                "The explanation should cover the principle of a simple pendulum.",
                "The prediction of the period of oscillation should be numerically accurate based on the given conditions."]
        elif t["experiment"] == "free_fall":
            criteria = [
                "The explanation should cover the principle of free fall.",
                "The prediction of the time for the object to fall should be numerically accurate based on the given conditions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
