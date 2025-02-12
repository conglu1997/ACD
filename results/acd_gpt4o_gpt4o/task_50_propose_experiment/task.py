class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"hypothesis": "Plants grow faster under blue light than red light."},
            "2": {"hypothesis": "Water with a higher pH level improves athletic performance."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to propose a scientific experiment to test the following hypothesis:

Hypothesis: {t['hypothesis']}

Your proposal should include:
1. A detailed description of the experimental setup.
2. The variables to be measured and controlled.
3. The procedure to be followed.
4. The method of data analysis.

Ensure your proposal is clear, logical, and scientifically sound. Provide your proposal in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The experimental setup should be detailed and feasible.", "Variables to be measured and controlled should be clearly identified.", "The procedure should be logical and step-by-step.", "The method of data analysis should be appropriate for the hypothesis."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
