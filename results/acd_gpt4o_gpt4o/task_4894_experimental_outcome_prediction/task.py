class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"initial_conditions": "A petri dish with nutrient agar is inoculated with a single E. coli bacterium and incubated at 37°C with shaking at 200 RPM for 24 hours. Antibiotics are not present.", "experiment": "bacterial_growth"},
            "2": {"initial_conditions": "A sealed container with 100 ml of water and 10 ml of pure ethanol is placed in a freezer set to -20°C. The temperature of the mixture is initially 25°C.", "experiment": "ethanol_water_freezing"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to predict the outcome of the following experiment based on the given initial conditions:

Initial Conditions: {t['initial_conditions']}

Ensure your prediction is based on scientific reasoning and includes an explanation of the underlying principles of the system. Provide your prediction in plain text format.

Desired format:
Prediction: [Your prediction]
Explanation: [Your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The prediction should be scientifically accurate and plausible.",
            "The explanation should demonstrate an understanding of the underlying principles of the system.",
            "The response should be coherent and logically structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
