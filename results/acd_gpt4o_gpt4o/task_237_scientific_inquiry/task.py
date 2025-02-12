class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'observation': 'In a garden, plants under the shade of a tree grow taller but have fewer flowers compared to plants in direct sunlight.'
            },
            '2': {
                'observation': 'Fish in a tank with a bubbler for aeration appear more active and have brighter colors compared to fish in a tank without a bubbler.'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            'Based on the given observation, your task is to formulate a scientific hypothesis and design an experiment to test this hypothesis. '
            'Ensure your hypothesis is clear, testable, and logically structured. '
            'Your experimental design should include the following elements:\n\n'
            '1. Hypothesis\n'
            '2. Independent variable\n'
            '3. Dependent variable\n'
            '4. Control variables\n'
            '5. Experimental procedure\n'
            '6. Expected results and how they would validate or refute your hypothesis\n'
            'Provide your response in plain text format, ensuring it is detailed, logically structured, and free of ambiguities.'
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The hypothesis should be clear, testable, and logically structured.',
            'The independent variable should be correctly identified.',
            'The dependent variable should be correctly identified.',
            'Control variables should be appropriately listed.',
            'The experimental procedure should be detailed, logically structured, and feasible.',
            'The expected results should clearly indicate how they validate or refute the hypothesis.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
