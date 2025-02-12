class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A ball is dropped from a height of 10 meters. Predict the time it will take to hit the ground, assuming no air resistance. Use the acceleration due to gravity as 9.8m/s^2.", "type": "prediction"},
            "2": {"scenario": "A car is traveling at a speed of 20 m/s and comes to a stop in 5 seconds. Calculate the car's acceleration and the distance it traveled during this time.", "type": "calculation"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "prediction":
            return f"""Predict the outcome of the following physical scenario: '{t["scenario"]}'. Use basic principles of physics to provide your answer, and show any necessary calculations. Submit your response as a plain text string in the following format:

Prediction: [Your prediction here]

Calculations: [Your calculations here]"""
        else:
            return f"""Calculate the following physical quantities based on the given scenario: '{t["scenario"]}'. Use basic principles of physics to provide your answer, and show any necessary calculations. Submit your response as a plain text string in the following format:

Calculation: [Your calculation here]

Calculations: [Your calculations here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "prediction":
            criteria = ["The prediction should be based on correct application of physics principles and should include necessary calculations."]
        else:
            criteria = ["The calculation should be correct and based on appropriate physics formulas."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
