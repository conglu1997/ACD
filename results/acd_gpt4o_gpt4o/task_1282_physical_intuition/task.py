class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "A ball is dropped from a height of 10 meters in a vacuum. Predict the time it takes for the ball to hit the ground in seconds and explain the reasoning."},
            "2": {"prompt": "A car is moving at a constant speed on a straight road. Suddenly, the driver applies the brakes, causing the car to decelerate uniformly until it stops. Explain what happens to the objects inside the car and why this occurs based on physical laws."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to predict the outcome of the following physical scenario or explain the physical phenomenon described:

Prompt: {t['prompt']}

For Task 1: Provide a prediction of the time it takes for the ball to hit the ground in seconds and explain your reasoning based on the principles of physics. Ensure your response is clear and concise.
For Task 2: Describe what happens to the objects inside the car and explain why this occurs based on physical laws. Ensure your response is logical and detailed.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should correctly predict the outcome or explain the phenomenon.",
            "The explanation should be based on established physical principles.",
            "The response should be logical and coherent.",
            "The response should match the expected format." 
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
