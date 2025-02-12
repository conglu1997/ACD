class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "variables": {"A": [1, 2, 3], "B": [1, 2, 3], "C": [1, 2, 3]},
                "constraints": [
                    "A != B",
                    "B < C",
                    "A + B > 2"
                ]
            },
            "2": {
                "variables": {"X": [1, 2, 3, 4], "Y": [1, 2, 3, 4], "Z": [1, 2, 3, 4]},
                "constraints": [
                    "X + Y == Z",
                    "X != Z",
                    "Y - X < 2"
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following constraint satisfaction problem (CSP) based on the given variables and constraints:

Variables:
{t['variables']}

Constraints:
{t['constraints']}

Find a solution that satisfies all the constraints. Provide your solution in the format: 'A = [value], B = [value], C = [value]' for Task 1, or 'X = [value], Y = [value], Z = [value]' for Task 2. For example, 'A = 1, B = 2, C = 3'. Ensure that your solution adheres to all the given constraints."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        try:
            # Extract the variable assignments from the submission
            assignments = {var.strip(): int(val.strip()) for var, val in (part.split('=') for part in submission.split(','))}
            # Validate the constraints
            for constraint in t['constraints']:
                if not TaskFamily.validate_constraint(constraint, assignments):
                    return 0.0
            return 1.0
        except Exception as e:
            print(f"Error validating submission: {e}")
            return 0.0

    @staticmethod
    def validate_constraint(constraint: str, assignments: dict) -> bool:
        try:
            tokens = constraint.split()
            if tokens[1] == '!=':
                return assignments[tokens[0]] != assignments[tokens[2]]
            elif tokens[1] == '<':
                return assignments[tokens[0]] < assignments[tokens[2]]
            elif tokens[1] == '>':
                return assignments[tokens[0]] > assignments[tokens[2]]
            elif tokens[1] == '<=':
                return assignments[tokens[0]] <= assignments[tokens[2]]
            elif tokens[1] == '>=':
                return assignments[tokens[0]] >= assignments[tokens[2]]
            elif tokens[1] == '==':
                return assignments[tokens[0]] == assignments[tokens[2]]
            elif tokens[1] == '+':
                return assignments[tokens[0]] + assignments[tokens[2]] == assignments[tokens[4]]
            elif tokens[1] == '-':
                return assignments[tokens[0]] - assignments[tokens[2]] == assignments[tokens[4]]
            else:
                return False
        except Exception as e:
            print(f"Error parsing constraint '{constraint}': {e}")
            return False
