class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'sentence': 'The quick brown fox jumps over the lazy dog.',
                'transformation': 'Convert to passive voice.'
            },
            '2': {
                'sentence': 'She was reading a book in the library when it started to rain.',
                'transformation': 'Convert to a question and change the tense to future perfect continuous.'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Transform the given sentence by applying the specified syntactic change.

Sentence: {t['sentence']}
Transformation: {t['transformation']}

Ensure that your transformed sentence is grammatically correct and accurately reflects the specified change. Submit your response as a plain text string.

Example response format:
Transformed Sentence: [Your transformed sentence]

Example:
Sentence: 'The cat chased the mouse.'
Transformation: 'Convert to passive voice.'
Transformed Sentence: 'The mouse was chased by the cat.'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            'The transformed sentence should be grammatically correct.',
            'The transformed sentence should accurately reflect the specified syntactic change.',
            'The response should be logical and coherent.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
