class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A plant in a garden is wilting. The weather has been hot and dry for the past week, and the plant has not been watered during this time.",
                "question": "What is the likely cause of the plant wilting?"
            },
            "2": {
                "scenario": "A car won't start. The battery was recently replaced, and the fuel tank is full. However, the car has not been serviced in a long time, and the engine makes a clicking sound when the ignition is turned on. Additionally, the car has been exposed to cold weather for several days. There are no visible signs of fluid leaks.",
                "question": "What is the likely cause of the car not starting?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Read the scenario and answer the question about the likely cause or effect.

Scenario: {t['scenario']}

Question: {t['question']}

Submit your response as a plain text string in the following format:

Response: [Your Answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should accurately identify the cause or effect based on the given scenario.",
            "The reasoning should be logical and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
