class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"hypothesis": "Plants grow faster when exposed to classical music."},
            "2": {"hypothesis": "The presence of a magnet affects the orientation of iron filings."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        hypothesis = t["hypothesis"]
        return f"""Design an experiment to test the following hypothesis: '{hypothesis}'. Ensure that your experimental design includes the following components and is clear, logical, and feasible:

1. A clear statement of the hypothesis.
2. A detailed description of the experimental setup, including any materials needed.
3. The variables to be measured and how they will be measured.
4. The control and experimental groups, if applicable.
5. The procedure for conducting the experiment, step by step.
6. The expected results and how they will be interpreted to support or refute the hypothesis.

Submit your experimental design as a plain text string in the following format:

Hypothesis: [Your statement of the hypothesis]
Experimental Setup: [Detailed description of the setup]
Materials: [List of materials needed]
Variables: [List of variables to be measured and how]
Groups: [Description of control and experimental groups]
Procedure: [Step-by-step procedure]
Expected Results: [Description of expected results and their interpretation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The experimental design should include all required components.",
            "The experiment should be logically structured and feasible.",
            "The materials, variables, control groups, and procedure should be clearly described.",
            "The expected results should logically follow from the experiment and support or refute the hypothesis."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
