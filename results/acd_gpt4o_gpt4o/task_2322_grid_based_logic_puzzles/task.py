class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"grid_size": 4, "constraints": ["A is not in the same row as B.", "C is in the column to the right of D.", "E is in the same row as F."]},
            "2": {"grid_size": 5, "constraints": ["G is in the top row.", "H is not adjacent to I.", "J is in the same column as K.", "L is to the left of M."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        grid_size = t["grid_size"]
        constraints = "\n".join(t["constraints"])
        instructions = f"""Your task is to perform two activities related to grid-based logic puzzles.

1. Solve the following grid-based logic puzzle by arranging the elements in a {grid_size}x{grid_size} grid according to the given constraints.
Constraints:
{constraints}

Provide your solution as a list of rows, where each row is a list of elements. For example:
[[A, B, C, D], [E, F, G, H], [I, J, K, L], [M, N, O, P]]

2. Generate a new grid-based logic puzzle of size {grid_size}x{grid_size}. Ensure that the puzzle has a unique solution and provide a set of constraints that lead to this solution. Provide the generated puzzle in the following format:
- Grid: [[element1, element2, ..., element{grid_size}], ..., [element{grid_size*(grid_size-1)+1}, ..., element{grid_size*grid_size}]]
- Constraints: [Your constraints]

Example for a 4x4 grid:
- Grid: [[A, B, C, D], [E, F, G, H], [I, J, K, L], [M, N, O, P]]
- Constraints: ['A is not in the same row as B.', 'C is in the column to the right of D.', 'E is in the same row as F.']"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution grid should satisfy all the given constraints.",
            "The generated puzzle should be of the specified grid size and have a unique solution.",
            "The constraints for the generated puzzle should be clear and lead to the unique solution."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
