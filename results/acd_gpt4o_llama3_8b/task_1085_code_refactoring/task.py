class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'code': '''
                def calculate_factors(n):
                    factors = []
                    for i in range(1, n + 1):
                        if n % i == 0:
                            factors.append(i)
                    return factors
                ''',
                'context': 'A function to calculate all factors of a given number.'
            },
            '2': {
                'code': '''
                def find_primes(limit):
                    primes = []
                    for num in range(2, limit + 1):
                        is_prime = True
                        for i in range(2, int(num ** 0.5) + 1):
                            if num % i == 0:
                                is_prime = False
                                break
                        if is_prime:
                            primes.append(num)
                    return primes
                ''',
                'context': 'A function to find all prime numbers up to a given limit.'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Refactor the following code snippet to improve its readability, efficiency, and maintainability without changing its functionality. Provide comments on what changes you made and why.

Code Snippet:
{t['code']}

Context: {t['context']}

Submit your refactored code and comments as a plain text string in the following format:

Refactored Code:
[Your refactored code]

Comments:
[Your comments]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            'The refactored code should maintain the same functionality as the original code.',
            'The refactored code should be more readable, efficient, and maintainable.',
            'The comments should clearly explain the changes made and the reasons for those changes.',
            'The submission should be well-organized and clearly written.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
