class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "grid": [
                    ["S", "0", "1"],
                    ["1", "0", "1"],
                    ["0", "0", "T"]
                ],
                "instructions": "You are given a 3x3 grid where 'S' is the starting point, 'T' is the target destination, '0' represents free space, and '1' represents obstacles. Provide the shortest path from 'S' to 'T' as a sequence of moves (U for up, D for down, L for left, R for right). For example, a path 'DR' means move down and then right."
            },
            "2": {
                "grid": [
                    ["S", "1", "0", "0"],
                    ["0", "1", "1", "0"],
                    ["0", "0", "0", "0"],
                    ["1", "1", "1", "T"]
                ],
                "instructions": "You are given a 4x4 grid where 'S' is the starting point, 'T' is the target destination, '0' represents free space, and '1' represents obstacles. Provide the shortest path from 'S' to 'T' as a sequence of moves (U for up, D for down, L for left, R for right). For example, a path 'DR' means move down and then right."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return t["instructions"]

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        # Provide the correct answers for the grids
        correct_paths = {
            "1": "DRDR",
            "2": "DRDDRDD"
        }
        # Determine the correct path based on the grid configuration
        if t["grid"] == [
            ["S", "0", "1"],
            ["1", "0", "1"],
            ["0", "0", "T"]
        ]:
            correct_path = correct_paths["1"]
        else:
            correct_path = correct_paths["2"]
        criteria = [
            "The path must be a sequence of moves using 'U', 'D', 'L', 'R'.",
            f"The path must match the correct sequence: {correct_path}."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
