class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"hypothesis": "Plants grow faster when exposed to classical music."},
            "2": {"hypothesis": "Drinking coffee before a test improves cognitive performance."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given hypothesis:

Hypothesis: {t['hypothesis']}

Your task is to simulate the scientific method by performing the following steps:
1. Formulate a hypothesis based on the given statement.
2. Design an experiment to test this hypothesis. Your design should include the materials needed, the procedure, and how you will measure the results.
3. Predict the possible outcomes of the experiment and how they would support or refute the hypothesis.
4. Draw a conclusion based on the predicted outcomes.

Ensure that your response is coherent, logically structured, and follows the scientific method. Submit your response as a plain text string in the following format:

Hypothesis:
[Your formulated hypothesis]

Experiment Design:
[Details of your experiment design]

Predicted Outcomes:
[Your predicted outcomes]

Conclusion:
[Your conclusion based on the outcomes]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include a hypothesis, a detailed experiment design (including materials, procedure, and measurement), predicted outcomes, and a conclusion.", "The experiment design should be logically sound and feasible.", "The conclusion should logically follow from the predicted outcomes."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
