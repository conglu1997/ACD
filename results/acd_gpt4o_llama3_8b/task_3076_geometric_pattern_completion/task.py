class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "sequence": [
                    [3],  # Triangle with 3 sides
                    [4],  # Square with 4 sides
                    [5],  # Pentagon with 5 sides
                    [6]   # Hexagon with 6 sides
                ]
            },
            "2": {
                "sequence": [
                    [2],  # Line with 2 points
                    [4],  # Square with 4 points
                    [6],  # Hexagon with 6 points
                    [8]   # Octagon with 8 points
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Identify the pattern in the following sequence of geometric shapes and predict the next shape in the sequence.

Sequence: {t['sequence']}

Provide your prediction as a list of integers representing the points or sides of the next shape in the sequence. The response should be a single list of integers."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        # The correct answers for the provided tasks
        correct_answers = {
            "1": [7],  # Heptagon with 7 sides
            "2": [10]  # Decagon with 10 points
        }
        task_id = list(t.keys())[0]
        # Criteria focuses on the correctness of the pattern
        criteria = ["The response should correctly identify the next shape in the sequence based on the pattern."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
