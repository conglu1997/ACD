class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "animals", "word": "elephant"},
            "2": {"theme": "fruits", "word": "banana"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a word puzzle based on the given theme and word. You can choose to create a crossword clue, anagram, word search, or any other type of word puzzle. Ensure that the puzzle is challenging yet solvable based on the given word and theme. Provide your puzzle in the following format:

Theme: {t['theme']}
Word: {t['word']}
Puzzle: [Your word puzzle here]

Example:
Theme: Animals
Word: Dog
Puzzle: A three-letter animal that barks (crossword clue)"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The puzzle should be based on the given word and theme.",
            "The puzzle should be challenging yet solvable.",
            "The puzzle should be creative and engaging.",
            "The puzzle should not be too easy or too hard.",
            "The puzzle should be correct and follow standard rules of the chosen puzzle type.",
            "The puzzle should be clearly stated and unambiguous."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
