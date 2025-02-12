import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "proverb": "A bird in the hand is worth __ in the __",
                "equation": "2x + 3y = 17",
                "constraint": "x < y and x > 0 and y > 0 and x.is_integer() and y.is_integer()"
            },
            "2": {
                "proverb": "__ hands make __ work",
                "equation": "x^2 - y = 32",
                "constraint": "x > 0 and y > 0 and x.is_integer() and y.is_integer()"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""This task involves mathematical problem-solving and linguistic creativity. Follow these steps for both tasks in the family:

1. Solve the given equations for both tasks. The solutions must satisfy the given constraints and use integer values for x and y.
   Task 1 equation: {TaskFamily.get_tasks()["1"]["equation"]}, constraint: {TaskFamily.get_tasks()["1"]["constraint"]}
   Task 2 equation: {TaskFamily.get_tasks()["2"]["equation"]}, constraint: {TaskFamily.get_tasks()["2"]["constraint"]}

2. Use the integer values you found to complete the proverbs:
   Task 1 proverb: "{TaskFamily.get_tasks()["1"]["proverb"]}"
   Task 2 proverb: "{TaskFamily.get_tasks()["2"]["proverb"]}"
   The words you use to fill in the blanks must rhyme with each other and be common English words (no obscure or made-up words).

3. Provide a brief explanation (1-2 sentences) of each proverb's meaning.

Provide your answer in the following format for each task:
Task [number]:
Equation solution: x = [integer value], y = [integer value]
Completed proverb: [Your completed proverb]
Meaning: [Brief explanation of the proverb's meaning]

Example (not a solution, just a format illustration):
Task 1:
Equation solution: x = 3, y = 5
Completed proverb: A bird in the hand is worth three in the tree
Meaning: It's better to have a small but certain advantage than a mere potential of a greater one.

Adhere strictly to this format for both tasks to ensure accurate evaluation.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "Both equation solutions are mathematically correct, use integer values, and satisfy the given constraints.",
            "Both proverbs are completed correctly using the respective solution values.",
            "For each proverb, the words used to complete it rhyme with each other and are common English words.",
            "A brief and accurate explanation of each proverb's meaning is provided.",
            "The submission adheres to the specified format for both tasks."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
