class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "A square with a side length of 4 units is rotated 45 degrees. What is the length of the diagonal after the rotation?", "answer": "4√2", "description": "Calculate the length of the diagonal of a square after a 45-degree rotation. Provide your answer in the form 'a√b' where a and b are integers."},
            "2": {"problem": "A rectangle has a length of 8 units and a width of 3 units. If the rectangle is scaled by a factor of 2 along its length and by a factor of 0.5 along its width, what are the new dimensions?", "answer": "16 units (length) and 1.5 units (width)", "description": "Determine the new dimensions of a rectangle after scaling its length and width by different factors. Provide your answer in the form 'length units (length) and width units (width)'."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        description = t["description"]
        instructions = f"""Your task is to solve the following geometric problem:\n\nProblem: {problem}\n\nDescription: {description}\n\nProvide your solution as a single value or a set of values in plain text format. Ensure that your solution adheres to the geometric principles described in the problem."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        answer = t["answer"].strip()
        submission = submission.strip()
        criteria = [f"The correct answer is {answer}."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
