class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "SEND + MORE = MONEY"},
            "2": {"puzzle": "EAT + THAT = APPLE"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following cryptarithm puzzle. Each letter represents a unique digit from 0 to 9. No two letters can represent the same digit. Provide the digit for each letter and ensure that the equation holds true.

Puzzle: {t['puzzle']}

Submit your solution in the following format:
A = [digit], B = [digit], ..., Z = [digit]

For example, if the puzzle is 'AB + CD = EF' and the solution is A=1, B=2, C=3, D=4, E=5, F=6, submit your solution as:
A = 1, B = 2, C = 3, D = 4, E = 5, F = 6"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution should provide a unique digit for each letter.", "The solution should satisfy the given equation."]
        # Additional validation: Parse submission and verify if the solution satisfies the equation.
        try:
            # Parse the submission
            mapping = {line.split(" = ")[0]: int(line.split(" = ")[1]) for line in submission.strip().split(", ")}
            # Verify the equation
            equation = t['puzzle'].replace(" ", "")
            for letter, digit in mapping.items():
                equation = equation.replace(letter, str(digit))
            left_side, right_side = equation.split('=')
            if eval(left_side) == int(right_side):
                return 1.0
            else:
                return 0.0
        except Exception as e:
            return 0.0
