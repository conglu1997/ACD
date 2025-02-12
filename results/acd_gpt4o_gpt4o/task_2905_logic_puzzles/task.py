class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle_type": "grid", "grid": [
                [" ", "1", " ", "4", " "],
                ["3", " ", " ", " ", "2"],
                [" ", " ", "5", " ", " "],
                ["2", " ", " ", " ", "3"],
                [" ", "4", " ", "1", " "]
            ], "rules": "Fill in the grid so that each row, each column, and each 3x3 subgrid contains all of the digits from 1 to 5 exactly once."},
            "2": {"puzzle_type": "logic_grid", "clues": [
                "The person who likes apples is not Alice.",
                "Bob likes oranges.",
                "The person who likes bananas is younger than the person who likes oranges.",
                "Charlie is older than the person who likes apples.",
                "Alice is younger than Bob but older than the person who likes bananas."
            ], "categories": [
                "Names: Alice, Bob, Charlie",
                "Fruits: apples, oranges, bananas",
                "Age: younger, middle, older"
            ]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["puzzle_type"] == "grid":
            grid = "\n".join([" ".join(row) for row in t["grid"]])
            rules = t["rules"]
            instructions = f"Solve the following grid puzzle based on these rules:\n\n{rules}\n\nGrid:\n{grid}\n\nProvide your solution by filling in the grid in plain text format, with each row on a new line and spaces between the numbers. For example, a valid submission could be:\n1 2 3 4 5\n5 4 3 2 1\n3 5 4 1 2\n2 1 5 3 4\n4 3 2 5 1"
        else:
            clues = "\n".join(t["clues"])
            categories = "\n".join(t["categories"])
            instructions = f"Solve the following logic grid puzzle based on these clues:\n\n{clues}\n\nCategories:\n{categories}\n\nProvide your solution in plain text format, specifying the matching of names, fruits, and ages. For example, a valid submission could be:\nAlice: apples, younger\nBob: oranges, middle\nCharlie: bananas, older"
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["puzzle_type"] == "grid":
            criteria = ["The grid should be correctly filled according to the rules provided."]
        else:
            criteria = ["The solution should correctly match names, fruits, and ages based on the clues provided."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
