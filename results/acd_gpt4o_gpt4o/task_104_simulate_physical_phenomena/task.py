class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"phenomenon": "projectile_motion", "parameters": {"initial_velocity": 20, "angle": 45, "gravity": 9.81}},
            "2": {"phenomenon": "simple_harmonic_motion", "parameters": {"mass": 1, "spring_constant": 10, "initial_displacement": 0.1, "time": 10}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['phenomenon'] == 'projectile_motion':
            return f"""Your task is to generate Python code to simulate the projectile motion of an object. The simulation should plot the trajectory of the object based on the given parameters.

Parameters:
Initial Velocity: {t['parameters']['initial_velocity']} m/s
Angle: {t['parameters']['angle']} degrees
Gravity: {t['parameters']['gravity']} m/s²

The code should calculate the time of flight, maximum height, and range of the projectile. Use appropriate physics equations and provide the output as a graph showing the trajectory of the projectile.

Provide your solution in the form of Python code. Ensure the code runs without errors and generates the correct plot."""
        elif t['phenomenon'] == 'simple_harmonic_motion':
            return f"""Your task is to generate Python code to simulate the simple harmonic motion of a mass-spring system. The simulation should plot the displacement of the mass over time based on the given parameters.

Parameters:
Mass: {t['parameters']['mass']} kg
Spring Constant: {t['parameters']['spring_constant']} N/m
Initial Displacement: {t['parameters']['initial_displacement']} m
Time: {t['parameters']['time']} s

The code should calculate the angular frequency and simulate the motion over the specified time period. Use appropriate physics equations and provide the output as a graph showing the displacement of the mass over time.

Provide your solution in the form of Python code. Ensure the code runs without errors and generates the correct plot."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The code should correctly simulate the specified physical phenomenon.", "The code should generate a plot that accurately represents the simulation.", "The code should use the given parameters correctly.", "The simulation should be based on appropriate physics equations.", "The code should be syntactically correct and run without errors."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
