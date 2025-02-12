class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"words": ["apple", "pear"]},
            "2": {"words": ["dog", "cat"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        words = ", ".join(t["words"])
        instructions = f"""Your task is to generate a small crossword puzzle using the following words: {words}.

1. Arrange the words in a crossword grid. Ensure that the words intersect where possible, and the grid is compact. Use a 3x3 grid for task 1 and a 3x3 grid for task 2.
2. Create a clue for each word. The clues should be clear, concise, and correspond to the words provided.
3. Provide the crossword grid and the clues in the following format:

Grid:
[Provide the grid layout here, using '.' for empty spaces and letters for filled spaces, with each row on a new line]
Clues:
- Word: [Clue]

Example:
Words: apple, pear
Grid:
a p p l e
. . . . .
p e a r .
Clues:
- apple: A fruit that keeps the doctor away.
- pear: A fruit that is similar to an apple but has a different shape.

Ensure that the puzzle is solvable and the clues are accurate and relevant to the words.
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The crossword grid should be compact and the words should intersect where possible.",
            "The clues should be accurate and relevant to the words.",
            "The puzzle should be solvable."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
