import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "topic": "astronomy",
                "example": "3 * 4 = 12 (Three times four equals twelve planets in our solar system)"
            },
            "2": {
                "topic": "environmental science",
                "example": "100 - 20 = 80 (One hundred minus twenty equals eighty percent of Earth's surface covered by water)"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create an original mathematical equation that, when read aloud, forms a coherent sentence in English related to the topic of {t['topic']}. The equation should be mathematically correct and, when read aloud, should form a grammatically correct and meaningful sentence.

Requirements:
1. The equation must be mathematically valid.
2. When read aloud, it must form a coherent English sentence related to the given topic.
3. Use only basic arithmetic operations (+, -, *, /) and integers.
4. The equation should have at least three terms and two operations.
5. Your equation and sentence must be original, not copied from the example.
6. Be creative! Avoid overly simple or trivial equations.

Example: {t['example']}

Provide your answer in the following format:
Equation: [Your equation here]
Sentence: [The sentence formed when reading the equation aloud]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submission contains both an equation and a sentence.",
            "The equation is mathematically correct and uses at least three terms and two operations.",
            f"The sentence is related to the topic of {t['topic']} and contains accurate information.",
            "The sentence is grammatically correct and meaningful.",
            "The sentence accurately represents the equation when read aloud.",
            "The equation and sentence are original creations, not copied from the example.",
            "The equation demonstrates creativity and is not overly simple or trivial."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
