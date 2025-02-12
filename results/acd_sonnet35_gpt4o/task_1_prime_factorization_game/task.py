import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"number": random.randint(50, 200), "game_rule": "largest"},
            "2": {"number": random.choice([random.randint(201, 500), random.choice([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])]), "game_rule": "smallest"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""This task consists of two steps:

1. Perform prime factorization on the number {t['number']}. Prime factorization is the process of decomposing a number into a product of prime numbers. Express your answer as a list of prime factors in ascending order. If the number itself is prime, the list should contain only that number.

2. You are playing a game with an opponent. You both have the prime factors you found in step 1. The game rule is to choose the {t['game_rule']} prime factor. Your opponent will choose randomly. If you both choose the same factor, you win. If you choose different factors, the player who chose the {t['game_rule']} factor wins.

What prime factor should you choose to maximize your chances of winning? Consider that choosing the {t['game_rule']} prime factor gives you the best chance of winning, as it ensures you win in all cases except when your opponent happens to choose the same factor.

Provide your answer in the following format:
Prime factorization: [list of prime factors]
Chosen factor for the game: [your chosen factor]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The prime factorization of {t['number']} is correct.",
            f"The chosen factor for the game is a valid prime factor of {t['number']}.",
            f"The chosen factor is the {t['game_rule']} prime factor, which maximizes the chance of winning.",
            "The response format is correct."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
