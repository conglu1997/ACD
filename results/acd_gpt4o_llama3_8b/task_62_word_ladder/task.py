class TaskFamily:
    # Predefined list of valid English words
    VALID_WORDS = set(['cat', 'cot', 'dot', 'dog', 'head', 'heal', 'teal', 'tell', 'tall', 'tail', 'heat', 'meat', 'mate', 'late', 'lake', 'bake', 'bale', 'bile', 'mile', 'file', 'tile'])

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "start_word": "cat",
                "end_word": "dog",
                "steps": 3
            },
            "2": {
                "start_word": "head",
                "end_word": "tail",
                "steps": 4
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate or solve a word ladder by transforming the word '{t['start_word']}' into the word '{t['end_word']}' in exactly {t['steps']} steps. Each step must change exactly one letter to form a new valid English word. Ensure that the initial word is '{t['start_word']}', the final word is '{t['end_word']}', and there are exactly {t['steps']} words in between (for a total of {t['steps'] + 1} words including the start and end words). Submit your solution as a plain text string with each word on a new line."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        words_list = submission.split('\n')
        if len(words_list) != t['steps'] + 2 or words_list[0] != t['start_word'] or words_list[-1] != t['end_word']:
            return 0.0
        for i in range(len(words_list) - 1):
            if len(words_list[i]) != len(words_list[i + 1]) or sum(a != b for a, b in zip(words_list[i], words_list[i + 1])) != 1 or words_list[i] not in TaskFamily.VALID_WORDS or words_list[i + 1] not in TaskFamily.VALID_WORDS:
                return 0.0
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
