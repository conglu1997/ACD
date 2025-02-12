class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "Fruit",
                "type": "crossword",
                "constraints": "The crossword should include at least 5 different types of fruit and should fit within a 5x5 grid."
            },
            "2": {
                "theme": "Animals",
                "type": "word_search",
                "constraints": "The word search should include at least 8 different animals and should fit within a 7x7 grid."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a {t['type']} puzzle based on the given theme and constraints. Ensure that the puzzle is correctly structured and solvable.

Theme: {t['theme']}

Constraints: {t['constraints']}

Response Format:
Provide the puzzle in plain text format.

For crosswords, use '#' for blank spaces and letters for filled spaces. Each row should be a new line and letters should be uppercase. Example:
A P P L E
P # # # #
P # # # #
L # # # #
E # # # #

For word searches, provide the grid with letters in uppercase and a list of words to find. Each row should be a new line and letters should be separated by spaces. Example:
A E I O U
B C D F G
H I J K L
M N O P Q
R S T U V
Words to find: ["APPLE", "BANANA"]

Make sure the provided examples meet the theme and constraints given in the task."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['type'] == 'crossword':
            criteria = [
                "The crossword should include at least 5 different types of fruit.",
                "The crossword should fit within a 5x5 grid.",
                "The crossword should be correctly structured with valid words and solvable.",
                "The crossword should use '#' for blank spaces and letters should be uppercase.",
                "The crossword should include meaningful connections between words."
            ]
        else:
            criteria = [
                "The word search should include at least 8 different animals.",
                "The word search should fit within a 7x7 grid.",
                "The word search should be correctly structured and solvable.",
                "The word search should use uppercase letters and provide a list of words to find.",
                "The words in the word search should be placed in meaningful directions (horizontal, vertical, diagonal)."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
