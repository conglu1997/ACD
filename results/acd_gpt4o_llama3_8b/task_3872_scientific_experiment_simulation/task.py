class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"experiment": "An experiment involves placing a 1-meter metal rod in a flame at one end and measuring the temperature at 10 cm intervals along the rod every 30 seconds for a duration of 5 minutes. The rod is made of copper, which has a high thermal conductivity."},
            "2": {"experiment": "A sunflower plant is placed in a sealed container with 1 liter of water and exposed to continuous light (24 hours per day) for a period of 7 days. The experiment aims to measure the rate of photosynthesis and growth of the plant over this period."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        experiment = t["experiment"]
        return f"""Simulate the following scientific experiment and predict the outcome based on the given conditions:\n\n{experiment}\n\nProvide your prediction with detailed reasoning. Submit your prediction as a plain text string in the following format:\n\nHypothesis: [Your hypothesis]\nSimulation Steps: [Description of steps to simulate the experiment]\nPrediction: [Your predicted outcome]\nReasoning: [Explanation of why you predict this outcome]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The hypothesis should be relevant to the experiment.",
            "The simulation steps should be logical and detailed.",
            "The prediction should be plausible given the conditions of the experiment.",
            "The reasoning should be clear and scientifically sound."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
