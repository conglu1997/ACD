class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'hypothesis': 'Plants grow faster when given fertilizer.'},
            '2': {'hypothesis': 'Students perform better on exams when they get at least 8 hours of sleep.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design a scientific experiment to test the following hypothesis:

Hypothesis: {t['hypothesis']}

Your experimental design should include the following elements:
1. A clear description of the independent and dependent variables.
2. An explanation of how you will control for other variables.
3. A description of the control group and the experimental group(s).
4. The expected outcomes if the hypothesis is correct.

Provide your experimental design in plain text format with clearly labeled sections for each element."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The experiment should clearly identify independent and dependent variables.',
            'The design should include control for other variables.',
            'There should be a clear description of control and experimental groups.',
            'The expected outcomes should logically follow from the hypothesis.',
            'The experimental design should be practical and feasible.',
            'The submission should follow the specified format with clearly labeled sections.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
