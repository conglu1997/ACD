class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "system": "A simple pendulum with a length of 2 meters and an initial angle of 30 degrees. Assume no air resistance and gravitational acceleration of 9.8 m/s^2.",
                "time": "10 seconds"
            },
            "2": {
                "system": "A projectile launched with an initial speed of 50 m/s at an angle of 45 degrees. Assume no air resistance and gravitational acceleration of 9.8 m/s^2.",
                "time": "5 seconds"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            "Your task is to predict the behavior of the given physical system under the specified conditions. "
            "Provide a detailed explanation of your reasoning process, the equations used, and the final prediction. "
            "Ensure that your prediction is consistent with the known physical laws and equations governing the system. "
            "Format your response as follows:\n\n"
            "1. System Description\n"
            "2. Initial Conditions\n"
            "3. Equations Used (with derivations if applicable)\n"
            "4. Step-by-Step Calculation\n"
            "5. Final Prediction (including the position, velocity, or other relevant quantities at the given time)\n"
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The prediction should be consistent with the known physical laws.",
            "The explanation should be detailed and logically sound.",
            "The final prediction should be accurate for the given time interval.",
            "The response should follow the specified format.",
            "The equations used should be correctly applied to the problem.",
            "Derivations should be included where necessary."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
