class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "solve", "puzzle": "Fill in the missing numbers in the following 3x3 magic square where the sum of each row, column, and diagonal is 15. Some numbers are already provided:\n\n_ 7 6\n9 _ 1\n4 3 _"},
            "2": {"type": "generate", "constraint": "Generate a sequence of 5 numbers where each number is the sum of the previous two numbers, starting with 1 and 1."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'solve':
            return f"Solve the following mathematical puzzle:\n\n{t['puzzle']}\n\nSubmit your solution as a plain text string in the following format:\nRow 1: [number] [number] [number]\nRow 2: [number] [number] [number]\nRow 3: [number] [number] [number]"
        elif t['type'] == 'generate':
            return f"Generate a sequence based on the following constraint:\n\n{t['constraint']}\n\nSubmit your sequence as a plain text string with each number separated by a comma (e.g., 1, 1, 2, 3, 5)."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['type'] == 'solve':
            criteria = ["The solution should correctly fill in the missing numbers in the magic square to achieve the specified sums."]
        elif t['type'] == 'generate':
            criteria = ["The generated sequence should meet the given constraint."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
