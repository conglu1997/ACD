class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "type": "word",
                "instructions": "Create a crossword puzzle with at least 5 words on a grid of at least 5x5 cells. The words must be interconnected, and the puzzle must include both horizontal and vertical words. Provide the clues for each word."
            },
            "2": {
                "type": "number",
                "instructions": "Create a Sudoku puzzle with a unique solution. Ensure that the puzzle follows standard Sudoku rules and provide the solution."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'word':
            return "Create a crossword puzzle with at least 5 words on a grid of at least 5x5 cells. The words must be interconnected, and the puzzle must include both horizontal and vertical words. Provide the clues for each word. Use '.' for empty cells and label clues with numbers. Submit your puzzle and clues in the following format:\nPuzzle:\n[Your crossword grid here]\nClues:\n1. [Clue for word 1]\n2. [Clue for word 2]\n...\nExample:\nPuzzle:\n. . . . .\n. 1 . 2 .\n. . . . .\n3 . . 4 .\n. . . . 5\nClues:\n1. First word clue\n2. Second word clue\n3. Third word clue\n4. Fourth word clue\n5. Fifth word clue"
        elif t['type'] == 'number':
            return "Create a Sudoku puzzle with a unique solution. Ensure that the puzzle follows standard Sudoku rules (each row, column, and 3x3 subgrid must contain all digits from 1 to 9 exactly once). Provide the solution. Use '.' for empty cells. Submit your puzzle and solution in the following format:\nPuzzle:\n[Your Sudoku puzzle here]\nSolution:\n[Your Sudoku solution here]\nExample:\nPuzzle:\n5 3 . . 7 . . . .\n6 . . 1 9 5 . . .\n. 9 8 . . . . 6 .\n8 . . . 6 . . . 3\n4 . . 8 . 3 . . 1\n7 . . . 2 . . . 6\n. 6 . . . . 2 8 .\n. . . 4 1 9 . . 5\n. . . . 8 . . 7 9\nSolution:\n5 3 4 6 7 8 9 1 2\n6 7 2 1 9 5 3 4 8\n1 9 8 3 4 2 5 6 7\n8 5 9 7 6 1 4 2 3\n4 2 6 8 5 3 7 9 1\n7 1 3 9 2 4 8 5 6\n9 6 1 5 3 7 2 8 4\n2 8 7 4 1 9 6 3 5\n3 4 5 2 8 6 1 7 9"
        return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = []
        if t['type'] == 'word':
            validation_criteria = [
                "The crossword must include at least 5 interconnected words.",
                "The puzzle must include both horizontal and vertical words.",
                "The puzzle must be on a grid of at least 5x5 cells.",
                "Provide clues for each word.",
                "The puzzle should be solvable."]
        elif t['type'] == 'number':
            validation_criteria = [
                "The Sudoku puzzle must follow standard rules.",
                "The puzzle must have a unique solution.",
                "Provide the solution for the Sudoku puzzle."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
