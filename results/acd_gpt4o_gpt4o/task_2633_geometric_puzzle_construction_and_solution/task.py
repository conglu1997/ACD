class TaskFamily:
    import random
    
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'puzzle_type': 'tangram',
                'pieces': ['large_triangle', 'medium_triangle', 'small_triangle', 'square', 'parallelogram'],
                'constraints': 'All pieces must fit within a square frame without overlapping and should form a coherent shape.',
                'expected_result': 'A solution where all pieces fit within the square frame forming a coherent shape.'
            },
            '2': {
                'puzzle_type': 'pentomino',
                'pieces': ['L', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
                'constraints': 'All pieces must fit within a rectangular frame without overlapping and should form a coherent shape.',
                'expected_result': 'A solution where all pieces fit within the rectangular frame forming a coherent shape.'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the given {t['puzzle_type']} puzzle based on the provided constraints. Ensure that your construction is logically sound and adheres to the given constraints.

Puzzle Type: {t['puzzle_type']}
Pieces: {', '.join(t['pieces'])}
Constraints: {t['constraints']}

Provide your solution in the following format:

1. Description of the puzzle
2. Constraints
3. Solution: [Your solution should describe how each piece fits within the frame, ensuring no overlapping and forming a coherent shape.]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution must fit within the given frame without overlapping.",
            "All given pieces must be used in the solution.",
            "The solution should be logically sound and adhere to the provided constraints.",
            "The pieces should form a coherent shape that fits the frame."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
