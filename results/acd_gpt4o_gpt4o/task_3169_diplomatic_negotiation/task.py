class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'scenario': 'Two neighboring countries, A and B, are in conflict over the use of a shared river. Country A wants to build a dam to generate hydroelectric power, while Country B relies on the river for agriculture. Propose a diplomatic strategy for Country A to negotiate with Country B and reach a compromise that benefits both nations.',
                'roles': ['Country A', 'Country B'],
                'objectives': {'Country A': 'Build a dam for hydroelectric power', 'Country B': 'Ensure sufficient water supply for agriculture'}
            },
            '2': {
                'scenario': 'Two countries, X and Y, are negotiating a trade agreement. Country X wants to export its surplus of wheat to Country Y, while Country Y wants to protect its domestic farmers. Propose a diplomatic strategy for Country X to negotiate with Country Y and reach a mutually beneficial trade agreement.',
                'roles': ['Country X', 'Country Y'],
                'objectives': {'Country X': 'Export surplus wheat', 'Country Y': 'Protect domestic farmers'}
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to engage in a fictional diplomatic negotiation and propose a strategy to reach a compromise. Follow the steps below:

1. Read the given scenario and understand the objectives of both parties.
2. Propose a diplomatic strategy for the assigned country to negotiate with the other country.
3. Justify your proposed strategy, explaining how it addresses the objectives of both parties and leads to a mutually beneficial compromise.

Scenario: {t['scenario']}

Roles: {', '.join(t['roles'])}

Objectives:
- {t['roles'][0]}: {t['objectives'][t['roles'][0]]}
- {t['roles'][1]}: {t['objectives'][t['roles'][1]]}

Submit your strategy and justification in plain text format. Your response should include the following sections:

1. Strategy: [Your proposed strategy]
2. Justification: [Your justification for the strategy]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The proposed strategy should be clear and detailed.',
            'The strategy should address the objectives of both parties.',
            'The justification should explain how the strategy leads to a mutually beneficial compromise.',
            'The response should demonstrate understanding of strategic reasoning and persuasive communication.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
