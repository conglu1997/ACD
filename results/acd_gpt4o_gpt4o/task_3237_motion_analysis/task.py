class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "projectile", "initial_velocity": 20, "angle": 45, "gravity": 9.8},
            "2": {"type": "pendulum", "length": 2, "initial_angle": 30, "gravity": 9.8}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'projectile':
            return f"""Your task is to analyze the motion of a projectile. The projectile is launched with an initial velocity of {t['initial_velocity']} m/s at an angle of {t['angle']} degrees to the horizontal. The acceleration due to gravity is {t['gravity']} m/s^2.

Calculate the following:
1. The time of flight (in seconds).
2. The maximum height reached by the projectile (in meters).
3. The horizontal range of the projectile (in meters).

Provide your answers in plain text format, each on a new line, in the order of the questions. Ensure all numerical answers are accurate to two decimal places."""
        elif t['type'] == 'pendulum':
            return f"""Your task is to analyze the motion of a simple pendulum. The pendulum has a length of {t['length']} meters and is released from an initial angle of {t['initial_angle']} degrees from the vertical. The acceleration due to gravity is {t['gravity']} m/s^2.

Calculate the following:
1. The period of the pendulum (in seconds).
2. The maximum speed of the pendulum bob (in meters per second).

Provide your answers in plain text format, each on a new line, in the order of the questions. Ensure all numerical answers are accurate to two decimal places."""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        import math

        instructions = TaskFamily.get_instructions(t)
        criteria = []

        try:
            answers = [float(x.strip()) for x in submission.split('\n')]

            if t['type'] == 'projectile':
                initial_velocity = t['initial_velocity']
                angle = math.radians(t['angle'])
                gravity = t['gravity']

                time_of_flight = (2 * initial_velocity * math.sin(angle)) / gravity
                max_height = (initial_velocity**2 * math.sin(angle)**2) / (2 * gravity)
                range_ = (initial_velocity**2 * math.sin(2 * angle)) / gravity

                expected_answers = [round(time_of_flight, 2), round(max_height, 2), round(range_, 2)]

            elif t['type'] == 'pendulum':
                length = t['length']
                initial_angle = math.radians(t['initial_angle'])
                gravity = t['gravity']

                period = 2 * math.pi * math.sqrt(length / gravity)
                max_speed = math.sqrt(2 * gravity * length * (1 - math.cos(initial_angle)))

                expected_answers = [round(period, 2), round(max_speed, 2)]

            else:
                return 0.0

            if len(answers) != len(expected_answers):
                return 0.0

            for answer, expected in zip(answers, expected_answers):
                if not math.isclose(answer, expected, rel_tol=1e-2):
                    return 0.0

            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

        except (ValueError, IndexError):
            return 0.0
