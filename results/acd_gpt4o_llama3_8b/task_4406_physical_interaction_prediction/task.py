class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "Two identical cars, each with a mass of 1000 kg, are moving towards each other at a speed of 20 m/s on a frictionless surface. Predict what will happen when they collide head-on. Assume the collision is perfectly elastic."
            },
            "2": {
                "scenario": "A ball with a mass of 0.5 kg is dropped from a height of 10 meters in a vacuum. Predict the time it will take to hit the ground and describe its motion. Assume the acceleration due to gravity is 9.81 m/s^2."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Read the following scenario and predict the outcome of the physical interaction described:

Scenario: {t['scenario']}

Your prediction should include:
1. A detailed explanation of the physical principles involved.
2. The expected outcome.
3. Any assumptions you are making.

Submit your response as a plain text string in the following format:
- Explanation: [Your explanation of the physical principles involved]
- Outcome: [Your predicted outcome]
- Assumptions: [Any assumptions you are making]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should accurately describe the relevant physical principles.",
            "The outcome should be logically consistent with the explanation and the given scenario.",
            "Any assumptions made should be reasonable and clearly stated."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
