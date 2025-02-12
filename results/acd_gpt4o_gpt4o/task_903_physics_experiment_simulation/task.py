class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "experiment": "A ball is dropped from a height of 10 meters. Describe the motion of the ball and predict the time it will take to hit the ground."
            },
            "2": {
                "experiment": "A car accelerates from rest at a constant rate of 2 m/s^2. Predict the car's velocity after 5 seconds and the distance it will have traveled."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "experiment" in t:
            return (
                "Your task is to simulate and describe the results of the following physics experiment based on physical principles. \n\n"
                "Experiment: {experiment}\n\n"
                "Your response should include:\n"
                "1. A description of the motion involved.\n"
                "2. Predictions of the key outcomes (e.g., time, velocity, distance).\n"
                "3. A detailed explanation of the reasoning and calculations behind your predictions.\n"
                "Provide your response in plain text format, ensuring clarity and detail.").format(experiment=t['experiment'])
        return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge

        instructions = TaskFamily.get_instructions(t)
        criteria = []

        if t['experiment'] == "A ball is dropped from a height of 10 meters. Describe the motion of the ball and predict the time it will take to hit the ground.":
            correct_prediction = "The ball will fall freely under gravity and take approximately 1.43 seconds to hit the ground."
            criteria.append(f"The prediction should be {correct_prediction}.")
        elif t['experiment'] == "A car accelerates from rest at a constant rate of 2 m/s^2. Predict the car's velocity after 5 seconds and the distance it will have traveled.":
            correct_prediction = "The car's velocity will be 10 m/s and it will have traveled 25 meters."
            criteria.append(f"The prediction should be {correct_prediction}.")

        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
