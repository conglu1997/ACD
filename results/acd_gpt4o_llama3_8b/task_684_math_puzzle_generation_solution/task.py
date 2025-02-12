class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "puzzle_type": "number_sequence",
                "sequence": "2, 3, 5, 7, 11, ?"
            },
            "2": {
                "puzzle_type": "algebraic_expression",
                "expression": "Solve for x: 2x + 3 = 11"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['puzzle_type'] == 'number_sequence':
            return f"""Identify the pattern in the given number sequence and provide the next number in the sequence.

Sequence: {t['sequence']}

Your response should include:
1. An explanation of the pattern identified.
2. The next number in the sequence.

Example response format:
- Pattern Explanation: The sequence consists of prime numbers.
- Next Number: 13

Ensure your explanation is clear, logical, and your solution is correct. Submit your response as a plain text string in the following format:
- Pattern Explanation: [Your explanation]
- Next Number: [Your solution]"""
        elif t['puzzle_type'] == 'algebraic_expression':
            return f"""Solve the given algebraic expression and provide the value of x.

Expression: {t['expression']}

Your response should include:
1. The steps taken to solve the expression.
2. The value of x.

Example response format:
- Steps: 2x + 3 = 11 => 2x = 8 => x = 4
- Solution: x = 4

Ensure your steps are clearly explained and your solution is correct. Submit your response as a plain text string in the following format:
- Steps: [Your steps]
- Solution: [Your solution]"""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['puzzle_type'] == 'number_sequence':
            criteria = [
                "The pattern explanation should correctly identify the underlying pattern in the sequence.",
                "The next number should logically follow the identified pattern."
            ]
        elif t['puzzle_type'] == 'algebraic_expression':
            criteria = [
                "The steps should logically lead to the solution.",
                "The value of x should be correct based on the given expression."
            ]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
