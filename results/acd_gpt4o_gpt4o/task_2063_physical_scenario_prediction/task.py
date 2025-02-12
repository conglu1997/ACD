class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A ball is rolling down a frictionless incline. The incline is 10 meters long and makes a 30-degree angle with the horizontal. Predict the velocity of the ball when it reaches the bottom of the incline.",
                "expected_output": "The velocity of the ball when it reaches the bottom of the incline is approximately 7.67 meters per second."
            },
            "2": {
                "scenario": "A block is pushed up a rough incline with an initial velocity of 5 meters per second. The incline is 5 meters long, makes a 45-degree angle with the horizontal, and has a coefficient of friction of 0.3. Predict whether the block will reach the top of the incline and, if not, how far it will travel.",
                "expected_output": "The block will not reach the top of the incline. It will travel approximately 2.96 meters before coming to a stop and sliding back down." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to predict the outcome of the given physical scenario based on the specified initial conditions.

Scenario: {t['scenario']}

Provide your prediction in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The prediction should correctly follow the principles of physics.",
            "The prediction should be quantitatively accurate as per the given initial conditions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
