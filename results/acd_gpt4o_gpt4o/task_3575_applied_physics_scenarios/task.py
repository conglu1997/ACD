class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A car of mass 1000 kg is traveling at a speed of 20 m/s. It comes to a stop after traveling 50 meters. Calculate the force exerted by the brakes to bring the car to a stop."},
            "2": {"scenario": "A satellite orbits the Earth at an altitude where the gravitational force is 70% of the force at the Earth's surface. Determine the altitude of the satellite above the Earth's surface."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following physics problem and provide a detailed explanation of the underlying principles.

Scenario: {t['scenario']}

Provide your solution in the following format:

Solution: [Your detailed solution and explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a correct and detailed solution to the physics problem.",
            "The response should explain the underlying principles used to solve the problem.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
