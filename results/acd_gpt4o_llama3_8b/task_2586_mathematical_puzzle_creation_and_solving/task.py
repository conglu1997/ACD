class TaskFamily:
    import random
    
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "rule": "Create a puzzle where the sum of any two adjacent numbers is a prime number. The puzzle should include exactly 5 distinct numbers between 1 and 20."
            },
            "2": {
                "puzzle": [2, 3, 5, 8, 13],
                "rule": "The sum of any two adjacent numbers should be a prime number."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "rule" in t:
            return f"""Complete the following task:

Create a mathematical puzzle based on the given rule. The puzzle should be a sequence of exactly 5 distinct numbers between 1 and 20. The rule is:
{t['rule']}

Submit your puzzle as a plain text string in the following format: [number1, number2, number3, number4, number5]

Sample response: [1, 3, 5, 7, 11]"""
        else:
            return f"""Complete the following task:

Solve the given mathematical puzzle based on the rule. The puzzle is a sequence of 5 numbers, and the rule is:
{t['rule']}

Puzzle: {t['puzzle']}

Submit your solution as a plain text string indicating whether the puzzle follows the rule or not. Your response should be either 'valid' or 'invalid'.

Sample response: valid"""

    @staticmethod
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "rule" in t:
            try:
                numbers = [int(x) for x in submission.strip('[]').split(',')]
                if len(numbers) != 5 or len(set(numbers)) != 5 or any(x < 1 or x > 20 for x in numbers):
                    return 0.0
                if all(TaskFamily.is_prime(numbers[i] + numbers[i + 1]) for i in range(4)):
                    return 1.0
                else:
                    return 0.0
            except Exception as e:
                return 0.0
        else:
            criteria = ["The submission should correctly indicate whether the puzzle follows the given rule or not."]
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
