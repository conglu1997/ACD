class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "criteria": "Generate a 5x5 Sudoku puzzle with 3 missing numbers."
            },
            "2": {
                "puzzle": [
                    [5, 3, 0, 0, 7],
                    [6, 0, 0, 1, 9],
                    [0, 9, 8, 0, 0],
                    [8, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0]
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'criteria' in t:
            return f"""Generate a visual puzzle based on the following criteria. Ensure the puzzle is logically coherent and solvable. Provide the puzzle as a plain text string in a format that clearly represents the visual layout.\n\nCriteria: {t['criteria']}\n\nExample response format:\n[[1, 2, 3, 4, 5],\n [6, 7, 8, 9, 0],\n [1, 2, 3, 4, 5],\n [6, 7, 8, 9, 0],\n [1, 2, 3, 4, 5]]"""
        elif 'puzzle' in t:
            return f"""Solve the following visual puzzle. Provide your solution as a plain text string in a format that clearly represents the visual layout.\n\nPuzzle: {t['puzzle']}\n\nExample response format:\n[[5, 3, 1, 2, 7],\n [6, 4, 2, 1, 9],\n [7, 9, 8, 3, 4],\n [8, 5, 3, 4, 6],\n [4, 6, 7, 5, 2]]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'criteria' in t:
            validation_criteria = [
                "The generated puzzle should be logically coherent.",
                "The puzzle should be solvable with the provided numbers."
            ]
        else:
            validation_criteria = [
                "The solution should correctly solve the puzzle.",
                "The solution should be presented in a clear format."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
