class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"observations": "Several species of birds have been observed migrating earlier in the year than usual over the past decade."},
            "2": {"observations": "A new plant species has been discovered in a region with high levels of metal contamination in the soil."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        observations = t['observations']
        return f"""Based on the following observations, generate a plausible scientific hypothesis:

Observations: {observations}

Ensure that your hypothesis is coherent, scientifically plausible, and directly related to the observations provided. The hypothesis should be concise, between 50 to 150 words. Submit your hypothesis as a plain text string.

Example Observation: Plants near a factory are showing signs of unusual growth patterns.
Example Hypothesis: The unusual growth patterns in plants near the factory may be due to the presence of chemical pollutants in the soil, which might be affecting the growth hormones in these plants."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
