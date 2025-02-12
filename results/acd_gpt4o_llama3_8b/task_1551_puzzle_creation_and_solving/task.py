class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "animals",
                "task_description": "Create a 5x5 crossword puzzle based on the given theme 'animals'. The puzzle should include at least 5 words related to the theme. Provide both the puzzle grid and the clues for each word. Format your response as follows: \n'Puzzle Grid: [Your 5x5 puzzle grid with words filled in, using dots for empty spaces] \nClues: [Your clues, numbered and corresponding to the positions in the grid]'. Example format for Puzzle Grid: \n..C.. \n.A.... \nTIGER \n....O \n...N. \nExample format for Clues: \n1. Across: This animal is known as the king of the jungle (5 letters). \n2. Down: A domesticated animal often kept as a pet (3 letters)."
            },
            "2": {
                "puzzle": "1. Across: A type of large cat known for its mane (5 letters). 2. Down: A marine mammal known for its intelligence (7 letters). 3. Across: A bird known for its colorful feathers (6 letters). 4. Down: A domesticated animal often kept as a pet (3 letters). 5. Across: A large flightless bird (7 letters).",
                "task_description": "Solve the provided crossword puzzle by identifying the correct words for each clue and placing them in the grid correctly. Format your response as follows: \n'Solutions: [Your solutions, in the format of a 5x5 grid with the correct letters in each position and dots for empty spaces]'. Example format for Solutions: \nLION. \n.D.... \nPARROT \n...G.. \n......."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return t['task_description']

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'theme' in t:
            validation_criteria = ["The puzzle should be engaging and solvable.", "The words should be relevant to the given theme.", "The clues should be clear and precise.", "The puzzle grid should be a valid 5x5 crossword."]
        else:
            validation_criteria = ["The solutions should correctly match the provided clues.", "The solutions should be placed correctly in a 5x5 grid."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
