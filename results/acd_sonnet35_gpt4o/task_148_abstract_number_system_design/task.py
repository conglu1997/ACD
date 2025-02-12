import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            "the life cycle of stars",
            "the stages of grief",
            "the color spectrum",
            "the water cycle"
        ]
        operations = ['+', '-', '*', '/']
        
        tasks = {
            "1": {
                "concept": random.choice(concepts),
                "operation1": random.choice(operations),
                "operation2": random.choice(operations),
                "number1": random.randint(1, 10),
                "number2": random.randint(1, 10),
                "number3": random.randint(1, 10)
            },
            "2": {
                "concept": random.choice(concepts),
                "operation1": random.choice(operations),
                "operation2": random.choice(operations),
                "number1": random.randint(1, 10),
                "number2": random.randint(1, 10),
                "number3": random.randint(1, 10)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel number system based on the concept of {t['concept']}. Your task has four parts:

1. Number System Design:
   a) Create a system to represent numbers using elements or stages from {t['concept']}.
   b) Explain how your system represents at least the numbers 0-10.
   c) Describe how your system handles larger numbers (if applicable).
   d) Explain why this number system is particularly suitable for representing {t['concept']}.

2. Arithmetic Operations:
   a) Explain how your system performs addition, subtraction, multiplication, and division.
   b) Provide an example for each operation using numbers from 0-10.

3. Problem Solving:
   Using your number system, solve the following problem:
   ({t['number1']} {t['operation1']} {t['number2']}) {t['operation2']} {t['number3']} = ?
   Show your work and explain each step.

4. Reflection:
   Discuss one advantage and one limitation of your number system compared to the decimal system.

Format your response as follows:

Number System Design:
[Your explanation here]

Arithmetic Operations:
[Your explanation and examples here]

Problem Solving:
[Your solution and explanation here]

Reflection:
[Your discussion here]

Ensure your number system is logically consistent, clearly explained, and truly based on the given concept. Be creative in your approach while maintaining mathematical validity."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a novel number system based on the given concept.",
            "The number system is logically consistent, clearly explained, and genuinely reflects the given concept (not just a renamed decimal system).",
            "The response explains how to perform basic arithmetic operations in the new system.",
            "The given problem is solved correctly using the new number system, with work shown and explained.",
            "The reflection provides insightful comparison between the new system and the decimal system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
