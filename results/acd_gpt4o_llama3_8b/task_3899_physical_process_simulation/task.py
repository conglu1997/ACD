class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "process": "fluid dynamics",
                "scenario": "Simulate the flow of water through a horizontal pipe with three different diameters: 2 cm, 4 cm, and 6 cm. The water enters the pipe at a speed of 1 m/s and a pressure of 100 kPa. Explain, using detailed calculations and relevant principles such as continuity and Bernoulli's equation, the changes in velocity and pressure at different points along the pipe."
            },
            "2": {
                "process": "mechanical system",
                "scenario": "Simulate the motion of a pendulum with a length of 1 meter and an initial angle of 30 degrees. Explain, using detailed calculations and principles of simple harmonic motion, how the period of the pendulum changes if the length is increased to 2 meters and if the initial angle is changed to 45 degrees."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Simulate and explain the following physical process based on the given scenario:

Process: {t['process']}
Scenario: {t['scenario']}

Ensure that your explanation includes relevant principles and equations, and that your simulation is coherent and logically consistent. Provide detailed descriptions and calculations where necessary. Submit your response as a plain text string in the following format:

Simulation:
1. [Your simulation description and calculations]

Explanation:
1. [Your detailed explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The simulation should be coherent and logically consistent.",
            "The explanation should include relevant principles and equations.",
            "The response should follow the specified format precisely.",
            "The descriptions and calculations should be detailed and accurate."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
