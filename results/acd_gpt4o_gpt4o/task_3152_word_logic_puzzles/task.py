class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "Find the next word in the sequence: cat, bat, rat, ?", "answer": "hat", "description": "Identify the pattern and find the next word in the sequence."},
            "2": {"puzzle": "Which word does not belong in the following list: apple, banana, carrot, grape, orange?", "answer": "carrot", "description": "Identify the word that does not fit the pattern in the list."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        puzzle = t["puzzle"]
        description = t["description"]
        instructions = f"""Your task is to solve the following word-based logic puzzle:\n\nPuzzle: {puzzle}\n\nDescription: {description}\n\nProvide your solution as a single word in plain text format. Ensure that your solution adheres to the pattern or logic described in the puzzle."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        answer = t["answer"].strip().lower()
        submission = submission.strip().lower()
        criteria = [f"The correct answer is {answer}."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
