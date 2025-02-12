class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'description': 'Generate a novel mathematical puzzle that involves prime numbers and provide its solution. The puzzle should be original and not a standard textbook problem. Ensure that the puzzle is challenging but solvable within a reasonable amount of time.'
            },
            '2': {
                'description': 'Create a mathematical puzzle that involves geometric shapes and their properties. The puzzle should be original and should require the solver to use properties of geometric shapes to arrive at the solution. Provide the solution to the puzzle as well.'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a novel mathematical puzzle based on the following description and provide its solution:

{t['description']}

Ensure that:
1. The puzzle is original and not a standard textbook problem.
2. The puzzle is challenging but solvable within a reasonable amount of time.
3. The solution is correct and clearly explained, with a detailed justification.
4. The puzzle should be unique and not a variation of a common problem.

Examples of novel puzzles:
- A puzzle involving prime numbers where the solution is a sequence or pattern that is not immediately obvious.
- A geometric puzzle where the solver needs to use properties of shapes to find a hidden relationship.

Submit your response in the following format:

Puzzle: [Your puzzle here]
Solution: [Your solution here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            'The puzzle is original and not a standard textbook problem.',
            'The puzzle is challenging but solvable within a reasonable amount of time.',
            'The solution is correct and clearly explained, with a detailed justification.',
            'The puzzle is unique and not a variation of a common problem.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
