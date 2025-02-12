class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "elements": ["A", "B", "C", "D"],
                "constraints": [
                    "A must be placed before B.",
                    "C cannot be placed next to D.",
                    "B must be placed immediately after A or C."
                ]
            },
            "2": {
                "elements": ["1", "2", "3", "4", "5"],
                "constraints": [
                    "1 must be placed before 3.",
                    "2 cannot be placed next to 4.",
                    "5 must be placed immediately after 2 or 3.",
                    "3 must be placed in the middle."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the combinatorial puzzle by arranging the elements to meet the specific constraints given. The elements are: {', '.join(t['elements'])}. The constraints are: {', '.join(t['constraints'])}. Submit your solution as a plain text string in the following format: 'Element1, Element2, Element3, ...'. Ensure that all constraints are satisfied in your final arrangement.

Example:
If the elements are [A, B, C] and the constraints are ['A must be before B', 'C cannot be next to A'], a valid solution could be 'B, A, C'. However, if the constraints were ['A must be before B', 'C must be after A'], a valid solution could be 'A, C, B'. Make sure to check all constraints against your solution."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The arrangement must include all elements.",
            "All constraints must be satisfied in the final arrangement.",
            "The order of elements must be explicitly stated."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
