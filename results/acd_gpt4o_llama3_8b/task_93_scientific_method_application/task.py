class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "hypothesis": "Plants grow faster when exposed to classical music.",
                "example": "Design an experiment to test if plants grow faster when exposed to classical music."
            },
            "2": {
                "hypothesis": "People solve puzzles more quickly after drinking coffee.",
                "example": "Design an experiment to test if people solve puzzles more quickly after drinking coffee."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a simple scientific experiment based on the following hypothesis: '{t['hypothesis']}'. Your experiment should include the following sections:
1. Introduction: Briefly explain the hypothesis and its significance.
2. Methodology: Describe the experimental setup, including the control and experimental groups, materials, and procedures.
3. Data Collection: Explain how you will collect and record data during the experiment.
4. Analysis: Describe how you will analyze the data to determine if the hypothesis is supported.
5. Conclusion: Summarize what conclusions you can draw from the experiment and any potential limitations.

Ensure your experiment design is clear, logical, and feasible. Provide enough detail in each section to demonstrate a thorough understanding of the scientific method."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The experiment design should be clear and logical.",
            "The methodology should include control and experimental groups.",
            "The data collection process should be well-defined.",
            "The analysis should be appropriate for the data collected.",
            "The conclusion should summarize potential findings and limitations."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
