class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Translate the following word problem into a mathematical expression and solve it: 'If a train travels 60 miles per hour and makes a 2-hour trip, how many miles does it travel in total?'", "criteria": "Correct translation and solution."},
            "2": {"description": "Translate the following word problem into a mathematical expression and solve it: 'A rectangle's length is 5 times its width. If the perimeter of the rectangle is 60 units, what are the dimensions of the rectangle?'", "criteria": "Correct translation and solution."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to translate the following word problem into a mathematical expression and solve it:\n\n{t['description']}\n\nProvide your response in the following format:\n\nMathematical Expression: [Your mathematical expression]\nSolution: [Your solution]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = t['criteria'].split(', ')
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
