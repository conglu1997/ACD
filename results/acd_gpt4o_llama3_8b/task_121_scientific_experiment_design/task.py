class TaskFamily:
    import random

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"hypothesis": "Plants grow faster in blue light than in red light."},
            "2": {"hypothesis": "Increasing the amount of sugar in a yeast solution will produce more carbon dioxide."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a simple scientific experiment to test the following hypothesis: '{t["hypothesis"]}'. Your experiment design should include the following components:

1. Objective: Clearly state the objective of your experiment.
2. Materials: List all the materials you will need.
3. Methods: Describe the step-by-step procedure you will follow.
4. Variables: Identify the independent, dependent, and controlled variables.
5. Data Collection: Explain how you will collect and analyze the data.
6. Expected Results: Describe what results you expect and how they will support or refute the hypothesis.

Submit your experiment design as a plain text string in the following format:

Objective: [Your objective]
Materials: [Your materials]
Methods: [Your step-by-step procedure]
Variables: [Your variables]
Data Collection: [Your data collection method]
Expected Results: [Your expected results]

Ensure that each component is clearly and thoroughly described."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The design should include a clear objective.",
            "The design should list all necessary materials.",
            "The methods should be described in a step-by-step manner.",
            "The independent, dependent, and controlled variables should be identified.",
            "The data collection and analysis methods should be explained.",
            "The expected results should be described and related to the hypothesis.",
            "Each component should be clearly and thoroughly described."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
