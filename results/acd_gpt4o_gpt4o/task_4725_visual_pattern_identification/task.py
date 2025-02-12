class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'pattern_description': 'A sequence of shapes that alternates between a square and a circle, increasing in size with each step. Starting with a 1x1 square, followed by a circle with a diameter of 2 units, then a 2x2 square, followed by a circle with a diameter of 4 units, and so on.',
                'visual_representation': 'Square(1x1), Circle(D=2), Square(2x2), Circle(D=4), ...'
            },
            '2': {
                'pattern_description': 'A sequence of numbers that doubles in value with each step, starting from 1. The sequence goes as follows: 1, 2, 4, 8, 16, 32, 64, ...',
                'visual_representation': '1, 2, 4, 8, 16, 32, 64, ...'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        pattern_description = t['pattern_description']
        visual_representation = t['visual_representation']
        return f'Your task is to identify the pattern described in the following set of visual instructions:\n\nPattern Description: {pattern_description}\nVisual Representation: {visual_representation}\n\nProvide a clear and concise description of the pattern, including any rules or regularities you observe. Your description should be in plain text format.'

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The description should accurately capture the pattern described in the visual instructions.',
            'The response should include a clear identification of the rule governing the pattern.',
            'The description should be detailed and specific, including any observed regularities.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
