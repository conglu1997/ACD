class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "You are given a set of 4 variables, each of which can take a value from 1 to 4. The constraints are: \n1. Variable A cannot be equal to Variable B.\n2. Variable C must be greater than Variable D.\n3. Variable B must be even.\n4. All variables must have different values.\nFind a valid assignment of values to the variables that satisfies all the constraints."},
            "2": {"description": "You are given a 4x4 Sudoku puzzle with some cells already filled. The constraints are: \n1. Each row must contain the numbers 1 to 4 with no repetition.\n2. Each column must contain the numbers 1 to 4 with no repetition.\n3. Each 2x2 subgrid must contain the numbers 1 to 4 with no repetition.\nFill in the missing numbers to complete the puzzle.\nInitial grid: [[1, 0, 0, 4], [0, 0, 3, 0], [0, 3, 0, 0], [4, 0, 0, 2]]"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        instructions = f"""Your task is to solve the constraint satisfaction problem described below:\n\n{description}\n\nProvide your solution in plain text format. For Task 1, list the values assigned to each variable (A, B, C, D). For Task 2, provide the completed 4x4 grid in the format of a nested list."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        task_1_criteria = ["The solution should assign distinct values to variables A, B, C, and D.", "Variable A should not be equal to Variable B.", "Variable C should be greater than Variable D.", "Variable B should be even."]
        task_2_criteria = ["Each row, column, and 2x2 subgrid should contain the numbers 1 to 4 with no repetition.", "The solution should correctly fill in the missing numbers in the initial grid."]
        if t == TaskFamily.get_tasks()["1"]:
            return 1.0 if eval_with_llm_judge(instructions, submission, task_1_criteria) else 0.0
        else:
            return 1.0 if eval_with_llm_judge(instructions, submission, task_2_criteria) else 0.0
