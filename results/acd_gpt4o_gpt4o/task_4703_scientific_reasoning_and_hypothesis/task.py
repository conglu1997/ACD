class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A plant species in a particular region is observed to have different leaf colors depending on the altitude at which it is found. Generate a hypothesis that could explain this observation and design an experiment to test your hypothesis. Include variables such as sunlight exposure, soil composition, and temperature variations at different altitudes."},
            "2": {"scenario": "In a controlled lab environment, a new chemical compound is found to react differently under varying temperatures. Generate a hypothesis to explain the different reactions and design an experiment to test your hypothesis. Include potential variables such as reaction time, concentration of the compound, and presence of catalysts."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a hypothesis based on the following scientific scenario and design an experiment to test your hypothesis:

{t["scenario"]}

Your response should include:
1. A clear and concise hypothesis.
2. A detailed experimental design that outlines the steps, controls, variables, and methods for testing your hypothesis.
3. An explanation of how the experiment will help confirm or refute your hypothesis.
Format your response in plain text. Ensure your response is logical, scientifically sound, and feasible."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The hypothesis should be clear and concise.",
            "The experimental design should be detailed and scientifically sound.",
            "The explanation should demonstrate how the experiment will test the hypothesis.",
            "The response should be logical and feasible."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
