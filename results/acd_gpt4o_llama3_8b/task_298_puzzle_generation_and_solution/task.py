class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "generation", "puzzle_type": "word search", "theme": "animals", "size": 10, "words": ["dog", "cat", "bird", "fish"], "constraints": "The word search must be a 10x10 grid and include all the given words hidden horizontally, vertically, or diagonally. The grid should be filled with random letters otherwise.", "example": "D O G X Y Z\nC A T B R D\nF I S H I J\nK L M N O P\nQ R S T U V\nW X Y Z A B\nC D E F G H\nI J K L M N\nO P Q R S T\nU V W X Y Z"},
            "2": {"task_type": "solution", "puzzle": "C A T X Y Z\nD O G B R D\nE F G H I J\nK L M N O P\nQ R S T U V\nW X Y Z A B\nC D E F G H\nI J K L M N\nO P Q R S T\nU V W X Y Z", "words": ["CAT", "DOG"], "example_solution": "CAT: (1,1) to (1,3)\nDOG: (2,1) to (2,3)"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "generation":
            return f"Generate a {t['puzzle_type']} puzzle based on the following criteria: Theme: {t['theme']}, Size: {t['size']}x{t['size']}, Words: {', '.join(t['words'])}. {t['constraints']} Ensure the word search is challenging and all words are well-hidden. Submit the puzzle as a plain text string in the following format: 'Grid:\n[grid lines]'.\nExample: {t['example']}"
        elif t["task_type"] == "solution":
            return f"Solve the following puzzle by finding the given words: Puzzle:\n{t['puzzle']}\nWords: {', '.join(t['words'])}. Submit the positions of each word in the format: 'Word: (start_row, start_col) to (end_row, end_col)'.\nExample Solution: {t['example_solution']}"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "generation":
            criteria = ["The generated word search must be a 10x10 grid, include all the specified words, and have random letters filling the remaining spaces. All words must be well-hidden and follow the given constraints."]
        elif t["task_type"] == "solution":
            criteria = ["The response should correctly identify the start and end positions of each word in the puzzle."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
