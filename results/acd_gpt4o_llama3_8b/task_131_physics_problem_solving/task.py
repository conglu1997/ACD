class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A car accelerates from rest to a speed of 20 m/s in 5 seconds. After reaching this speed, it maintains this velocity for 10 seconds before decelerating uniformly to a stop in 8 seconds. Calculate the car's acceleration during the first 5 seconds, the distance traveled during the constant velocity phase, and the deceleration during the last 8 seconds."},
            "2": {"scenario": "A projectile is launched with an initial velocity of 30 m/s at an angle of 45 degrees from the horizontal. Calculate the maximum height reached by the projectile, the total time of flight, and the horizontal range of the projectile. Assume no air resistance."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        return f"""Solve the following physics problem based on the given scenario:

Scenario: {scenario}

Provide your solution with detailed steps and calculations. Submit your solution as a plain text string in the following format:

Step 1: [Description of step and calculations]
Step 2: [Description of step and calculations]
...
Final Answer: [Your final answers]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should include detailed steps and calculations.",
            "The solution should be scientifically accurate.",
            "The final answers should be correct based on the given scenario."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
