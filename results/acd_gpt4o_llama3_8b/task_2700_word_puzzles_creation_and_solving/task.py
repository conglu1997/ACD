class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'puzzle_type': 'word_ladder',
                'start_word': 'cold',
                'end_word': 'warm',
                'steps': 4
            },
            '2': {
                'puzzle_type': 'crossword',
                'clues': [
                    {'clue': 'A fruit that is red and round', 'length': 5, 'answer': 'apple'},
                    {'clue': 'A four-legged animal that barks', 'length': 3, 'answer': 'dog'}
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['puzzle_type'] == 'word_ladder':
            return f"""Create a word ladder puzzle where the goal is to transform the start word to the end word in the given number of steps. Each step must change exactly one letter to form a valid English word.

Start word: {t['start_word']}
End word: {t['end_word']}
Steps: {t['steps']}

Submit your response as a plain text string in a sequence of words, each on a new line, starting with the start word and ending with the end word. Ensure each word in the sequence is a valid English word and only differs by one letter from the previous word."""
        elif t['puzzle_type'] == 'crossword':
            clues = '\n'.join([f"{i+1}. {clue['clue']} ({clue['length']} letters)" for i, clue in enumerate(t['clues'])])
            return f"""Solve the following crossword puzzle based on the given clues. Each answer should match the clue and fit the specified length.

Clues:
{clues}

Submit your answers in the same order as the clues, each on a new line, ensuring each answer matches the clue provided."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = []
        if t['puzzle_type'] == 'word_ladder':
            validation_criteria = [
                'The response should start with the start word and end with the end word.',
                'Each word in the sequence should differ by exactly one letter from the previous word.',
                'All words in the sequence should be valid English words.'
            ]
        elif t['puzzle_type'] == 'crossword':
            validation_criteria = [
                'Each submitted word should match the corresponding clue in meaning and length.',
                'The answers should be in the same order as the clues.'
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
