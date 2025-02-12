class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "experiment": "Determine the effect of different fertilizers on plant growth",
                "requirements": ["Use at least three different types of fertilizers", "Measure plant height over a period of 4 weeks"]
            },
            "2": {
                "experiment": "Investigate the relationship between temperature and solubility of salt in water",
                "requirements": ["Use at least three different temperatures", "Measure the amount of salt dissolved in a fixed volume of water"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Provide a detailed explanation and step-by-step procedure for conducting the following scientific experiment:

Experiment: {t['experiment']}

Requirements: {', '.join(t['requirements'])}

Your response should include:
1. An explanation of the scientific principles behind the experiment.
2. A step-by-step procedure for conducting the experiment, including materials needed, specific steps, and how to measure and record results.
3. Any safety precautions that should be taken.
4. The expected outcome of the experiment.

Example format:
Explanation: [Your explanation]
Procedure:
1. [Step 1]
2. [Step 2]
...
Safety Precautions: [Any safety precautions]
Expected Outcome: [Your expected outcome]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should accurately describe the scientific principles behind the experiment.",
            "The procedure should include all necessary steps, materials, and measurements, and should be clear and logically ordered.",
            "Any relevant safety precautions should be mentioned.",
            "The expected outcome should be scientifically plausible and logically derived from the experiment."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
