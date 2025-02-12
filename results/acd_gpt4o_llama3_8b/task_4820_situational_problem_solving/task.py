class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'scenario': 'You are the manager of a small retail store. Recently, there has been a noticeable decline in sales despite an increase in foot traffic. Diagnose the potential causes and propose solutions to address the issue.'},
            '2': {'scenario': 'You are the head of IT at a mid-sized company. The company has been experiencing frequent network outages, which are impacting productivity. Diagnose the potential causes and propose solutions to address the issue.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Read the following scenario and diagnose the potential causes of the problem described. Then, propose viable solutions to address the issue.

Scenario: {t['scenario']}

Your response should include:
1. A brief summary of the problem.
2. A diagnosis of the potential causes, with at least three distinct causes.
3. Proposed solutions to address each of the identified causes.

Submit your response as a plain text string with clearly labeled sections for 'Summary', 'Diagnosis', and 'Solutions'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The response should include a brief summary of the problem.',
            'The response should include a diagnosis of the potential causes, with at least three distinct causes.',
            'The response should include proposed solutions to address each of the identified causes.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
