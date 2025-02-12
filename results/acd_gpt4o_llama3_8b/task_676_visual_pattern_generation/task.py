class TaskFamily:
    import random
    
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'prompt': 'Generate a simple geometric pattern using circles and squares. The pattern should be symmetrical both horizontally and vertically and contain exactly 5 shapes: 3 circles and 2 squares.'
            },
            '2': {
                'prompt': 'Interpret the following visual pattern and describe it in detail: "O O O\n X X X\nO O O". Your description should include the shapes used, their arrangement, and any noticeable symmetries or patterns. Conclude with a possible use case for this pattern.'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the given prompt, perform the specified task:

Prompt: {t['prompt']}

For Task 1, submit your response as a plain text string in the format of a grid with your generated pattern. Use 'O' to represent circles and 'X' to represent squares, arranged in a symmetrical manner.
Example format:
O X O
X O X
O X O

For Task 2, submit your detailed description as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            'The response should correctly follow the given prompt.',
            'For Task 1, the pattern should be symmetrical both horizontally and vertically and contain exactly 5 shapes: 3 circles (O) and 2 squares (X).',
            'For Task 2, the description should be clear, detailed, and include a possible use case for the pattern.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
