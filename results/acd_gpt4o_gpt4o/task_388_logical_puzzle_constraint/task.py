class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "You are given a 3x3 grid. Place the numbers 1 to 9 in the grid such that each row, column, and diagonal adds up to 15. Provide your answer in a 3x3 matrix format like \n[[a, b, c],\n[d, e, f],\n[g, h, i]]. Make sure that no number is repeated in the grid and all constraints are satisfied."},
            "2": {"prompt": "You have a 4x4 grid with some cells already filled with numbers. Fill the remaining cells with numbers 1 to 4 such that no number repeats in any row, column, or 2x2 subgrid. The current grid is:\n[ [1, _, _, 4],\n  [_, 3, _, _],\n  [_, _, 2, _],\n  [2, _, _, 3] ]. Provide your answer in a 4x4 matrix format like \n[[a, b, c, d],\n[e, f, g, h],\n[i, j, k, l],\n[m, n, o, p]]. Make sure that all constraints are satisfied."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following logical puzzle. Ensure that you follow all the constraints mentioned in the prompt:\n\n{t['prompt']}\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
