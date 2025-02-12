class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"experiment": "Determine the concentration of an unknown salt solution using titration."},
            "2": {"experiment": "Investigate the effect of light intensity on the rate of photosynthesis in plants."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design a detailed experimental procedure for the following experiment:

Experiment: {t['experiment']}

Ensure that your procedure is clear, logically structured, and includes all necessary steps and materials. Provide your procedure in plain text format, structured as follows:

1. Objective: [State the objective of the experiment]
2. Materials: [List all materials and equipment needed]
3. Procedure: [Provide a step-by-step procedure for conducting the experiment]
4. Data Collection: [Describe how data will be collected and recorded]
5. Analysis: [Explain how the data will be analyzed to achieve the objective]

Make sure each section is detailed and easy to follow."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The procedure should be clear and logically structured.", "All necessary steps and materials should be included.", "The procedure should be appropriate for achieving the experiment's objective."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
