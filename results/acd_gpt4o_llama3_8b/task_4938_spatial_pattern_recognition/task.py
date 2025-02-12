class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "pattern_sequence": [
                    [0, 1, 0, 1],
                    [1, 0, 1, 0],
                    [0, 1, None, 1],
                    [1, 0, 1, 0]
                ],
                "missing_element_position": (2, 2)
            },
            "2": {
                "pattern_sequence": [
                    [0, 1, 1, 0],
                    [1, 0, 0, 1],
                    [0, 1, 1, 0],
                    [1, None, 0, 1]
                ],
                "missing_element_position": (3, 1)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        pattern_sequence = '\n'.join([' '.join(['_' if val is None else str(val) for val in row]) for row in t['pattern_sequence']])
        return f"""Identify the missing element in the following pattern sequence.

Pattern Sequence:
{pattern_sequence}

The position of the missing element is: {t['missing_element_position']}.

Submit your response as a plain text string indicating the value at the missing element position (0 or 1)."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        correct_value = TaskFamily._find_correct_value(t['pattern_sequence'], t['missing_element_position'])
        return 1.0 if submission.strip() == str(correct_value) else 0.0

    @staticmethod
    def _find_correct_value(pattern_sequence: list[list[int | None]], position: tuple[int, int]) -> int:
        # Implement the logic to find the correct value at the given position based on the pattern
        row, col = position
        if pattern_sequence[row][col] is not None:
            return pattern_sequence[row][col]
        # Example logic for determining the missing value based on alternating pattern
        return (pattern_sequence[row][col-1] + 1) % 2
