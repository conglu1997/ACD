class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {'parameters': 'Analyze the causes and effects of the Industrial Revolution and propose an alternative scenario where the revolution started 50 years earlier.'},
            '2': {'parameters': 'Analyze the key factors that led to the fall of the Roman Empire and propose an alternative scenario where the Empire managed to survive for another 200 years.'}
        }
        assert len(tasks) == 2, 'There should be exactly two tasks.'
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the following historical event and synthesize a new historical scenario based on the given parameters.

Parameters: {t['parameters']}

Provide a detailed analysis of the historical event, including its causes, key figures, and significant outcomes. Then, propose an alternative historical scenario based on the provided parameters. Your proposal should be logical, creative, and demonstrate a deep understanding of the historical context. Provide your response in plain text format.
Example format:
1. Analysis of Historical Event: [Detailed analysis of the event]
2. Alternative Scenario: [Description of the alternative scenario, including key differences and potential outcomes]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The response should include a detailed analysis of the historical event.',
            'The alternative scenario should be logically coherent and creative.',
            'The response should demonstrate a deep understanding of the historical context.',
            'The analysis should cover causes, key figures, and significant outcomes of the event.',
            'The alternative scenario should clearly explain the key differences and potential outcomes.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
