class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "Given a sequence of shapes: Circle, Triangle, Square, Circle, Triangle, what comes next?"},
            "2": {"puzzle": "In a 3x3 grid, the first two rows are filled with shapes in the following pattern: \nRow 1: Circle, Square, Triangle\nRow 2: Square, Triangle, Circle\nFill the third row to complete the pattern."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the geometric puzzle given below. Carefully analyze the pattern or sequence and provide the correct shape(s) to complete it.\n\nPuzzle: {t['puzzle']}\n\nProvide your answer in plain text format. For Task 1, provide a single shape as your answer. For Task 2, provide a sequence of shapes separated by commas in the order they should appear in the third row."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['puzzle'].startswith('Given a sequence of shapes'):
            criteria = ["The submission should be 'Square'."]
        else:
            criteria = ["The submission should be 'Triangle, Circle, Square'."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
