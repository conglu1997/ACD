class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A ball is thrown vertically upward with an initial velocity of 20 m/s from a height of 1.5 meters. Predict the time it will take for the ball to hit the ground and its velocity upon impact.", "initial_conditions": {"initial_velocity": 20, "initial_height": 1.5, "acceleration_due_to_gravity": 9.8}},
            "2": {"scenario": "A car traveling at 30 m/s begins to decelerate at a constant rate of 5 m/s² after passing a traffic signal. Predict the distance the car will travel before coming to a complete stop.", "initial_conditions": {"initial_velocity": 30, "deceleration": 5}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to simulate the following physical scenario and predict the outcomes based on the given initial conditions:

Scenario: {t['scenario']}

Initial Conditions:
- Initial velocity: {t['initial_conditions'].get('initial_velocity', 'N/A')} m/s
- Initial height: {t['initial_conditions'].get('initial_height', 'N/A')} meters
- Acceleration due to gravity: {t['initial_conditions'].get('acceleration_due_to_gravity', 'N/A')} m/s²
- Deceleration: {t['initial_conditions'].get('deceleration', 'N/A')} m/s²

Provide a detailed prediction of the outcomes, including:

1. For Task 1, the time it will take for the ball to hit the ground and the velocity of the ball upon impact.
2. For Task 2, the distance the car will travel before coming to a complete stop.
3. Any assumptions or simplifications you made in your calculations.

Provide your response in the following format:

Response:
- Time to hit the ground: [Your answer] seconds
- Velocity upon impact: [Your answer] m/s
- Distance traveled before stop: [Your answer] meters
- Assumptions: [Your assumptions]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The predictions should be accurate based on the given initial conditions.",
            "The explanation should be clear and logical.",
            "Any assumptions or simplifications should be reasonable and justifiable."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
