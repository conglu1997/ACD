class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"observations": "A group of plants in a controlled environment shows stunted growth compared to those in an open environment. Both groups receive the same amount of water and sunlight.", "description": "Generate a plausible scientific hypothesis to explain the stunted growth of plants in the controlled environment."},
            "2": {"observations": "In an experiment, a certain species of bacteria shows increased resistance to an antibiotic after being exposed to a low dosage of the antibiotic over several generations.", "description": "Generate a plausible scientific hypothesis to explain the increased resistance of the bacteria to the antibiotic."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        observations = t["observations"]
        description = t["description"]
        instructions = f"""Your task is to analyze the following observations and generate a plausible scientific hypothesis to explain them:\n\nObservations:\n{observations}\n\nDescription:\n{description}\n\nPlease provide your hypothesis in plain text format. Ensure that your hypothesis is scientifically sound, logically structured, and based on the given observations."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The hypothesis should be scientifically plausible and logically structured.",
            "The hypothesis should be based on the given observations and data.",
            "The hypothesis should be clearly articulated and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
