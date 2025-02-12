class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'hypothesis': 'Plants grow faster with blue light than with red light.'},
            '2': {'hypothesis': 'Increasing the concentration of sugar in water increases the rate of fermentation by yeast.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design an experiment to test the following hypothesis:

Hypothesis: {t['hypothesis']}

Your experimental design should include:
1. A clear description of the experimental setup.
2. Identification of the independent and dependent variables.
3. Description of the control group and how it will be used.
4. Step-by-step procedure of how the experiment will be conducted.
5. Any potential sources of error and how they will be mitigated.

Provide your experimental design in plain text format. Format your response as follows:

1. Experimental Setup:
2. Independent and Dependent Variables:
3. Control Group:
4. Procedure:
5. Potential Sources of Error:
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The response should include a clear description of the experimental setup.',
            'The response should identify the independent and dependent variables.',
            'The response should describe the control group and its use.',
            'The response should include a step-by-step procedure.',
            'The response should address potential sources of error.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
