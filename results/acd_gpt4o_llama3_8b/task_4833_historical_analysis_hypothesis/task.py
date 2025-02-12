class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'scenario': 'Analyze the possible causes and consequences of the fall of the Western Roman Empire in 476 AD. Provide a detailed explanation of at least three potential causes, supported by historical evidence, and predict the immediate and long-term impacts on European society. Focus on political, economic, and social aspects.'
            },
            '2': {
                'scenario': 'Consider an alternative history where the Industrial Revolution began in 1600 instead of 1800. How might this have affected the development of global political and economic systems, particularly in Europe and Asia? Provide a well-reasoned hypothesis supported by historical analogies. Discuss at least three significant changes in detail.'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following historical scenario and generate a detailed hypothesis:

Scenario: {t['scenario']}

Your response should include:
1. A thorough analysis of the scenario.
2. A well-reasoned hypothesis based on historical knowledge.
3. Predictions of the immediate and long-term impacts.

Ensure your hypothesis is logical, well-supported by historical facts, and clearly articulated. Submit your response as a plain text string in the following format:

Analysis: [Your analysis]
Hypothesis: [Your hypothesis]
Predictions: [Your predictions]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            'The response must include an analysis, a hypothesis, and predictions.',
            'The analysis should be thorough, covering political, economic, and social aspects where applicable.',
            'The hypothesis should be logical, well-reasoned, and supported by historical evidence or analogies.',
            'The predictions should be plausible and based on the hypothesis.',
            'Responses should be detailed and clearly articulated.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
