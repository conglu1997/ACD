class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"observation": "Plants growing near a light source grow faster than those in the shade."},
            "2": {"hypothesis": "Increasing the amount of sunlight a plant receives will increase its growth rate.", "experiment_results": "Plants exposed to 8 hours of sunlight per day grew 30% taller than those exposed to 4 hours per day over a month."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'observation' in t:
            return f"""Your task is to generate a scientific hypothesis based on the following observation:

Observation: {t['observation']}

Ensure your hypothesis is clear, testable, and based on scientific principles. Provide your hypothesis in plain text format."""
        else:
            return f"""Your task is to validate the following hypothesis using the provided experimental results. Discuss whether the results support or refute the hypothesis, and explain your reasoning clearly.

Hypothesis: {t['hypothesis']}

Experiment Results: {t['experiment_results']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'observation' in t:
            criteria = ["The hypothesis should be clear and testable.", "The hypothesis should be logically derived from the observation."]
        else:
            criteria = ["The validation should accurately interpret the experiment results.", "The reasoning should clearly explain whether the results support or refute the hypothesis."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
