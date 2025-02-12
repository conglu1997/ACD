import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        operations = ['+', '-', '*', '/']
        return {
            "1": {"operation": random.choice(operations), "difficulty": "easy", "number_range": (1, 20)},
            "2": {"operation": random.choice(operations), "difficulty": "hard", "number_range": (1, 100)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a simple constructed language (conlang) and use it to formulate a {t['difficulty']} mathematical word problem involving the '{t['operation']}' operation. Then, solve the problem. Follow these steps:

1. Conlang Creation (100-150 words):
   a) Invent 10-15 words for your conlang, including numbers (at least 0-10), and basic mathematical terms.
   b) Provide a brief explanation of the conlang's grammar, syntax, and number system.

2. Word Problem (50-75 words):
   a) Write a {t['difficulty']} mathematical word problem in your conlang using the '{t['operation']}' operation.
   b) Use numbers within the range of {t['number_range'][0]} to {t['number_range'][1]}.
   c) Provide an English translation of the problem.

3. Solution (50-75 words):
   a) Solve the word problem, showing your work.
   b) Explain your solution process using both your conlang and English.

Ensure your conlang is consistent and your word problem is solvable using the information provided."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The conlang is consistently defined with 10-15 words including numbers and mathematical terms.",
            "The conlang's grammar, syntax, and number system are briefly explained.",
            f"The word problem is written in the conlang, uses the '{t['operation']}' operation, and includes numbers within the specified range.",
            "An English translation of the word problem is provided.",
            "The solution is correct and the process is clearly explained using both the conlang and English.",
            f"The overall difficulty of the problem matches the '{t['difficulty']}' level specified."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
