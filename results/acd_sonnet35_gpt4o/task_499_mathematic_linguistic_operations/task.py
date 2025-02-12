import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        operations = [
            {"operation": "addition", "symbol": "+"},
            {"operation": "subtraction", "symbol": "-"},
            {"operation": "multiplication", "symbol": "*"},
            {"operation": "division", "symbol": "/"}
        ]
        return {
            "1": random.choice(operations),
            "2": random.choice(operations)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a linguistic transformation system to represent the mathematical operation of {t['operation']} (symbol: {t['symbol']}).

Your task has the following parts:

1. System Design (150-200 words):
   a) Describe your linguistic transformation system for representing {t['operation']}.
   b) Explain how your system captures the essential properties of this operation.
   c) Provide an example of how to represent a simple {t['operation']} operation (e.g., 3 {t['symbol']} 2) using your system.

2. Complex Expression (100-150 words):
   a) Create a more complex mathematical expression involving {t['operation']} and at least one other operation.
   b) Represent this expression using your linguistic transformation system.
   c) Explain the steps to evaluate this expression using your system.

3. Problem-Solving Application (150-200 words):
   a) Propose a real-world problem that can be solved using your linguistic representation of {t['operation']}.
   b) Describe how to solve this problem step-by-step using your system.
   c) Discuss any advantages or limitations of using your system for this problem compared to traditional mathematical notation.

4. Reflection (100-150 words):
   a) Discuss potential implications of your linguistic transformation system for mathematics education or cognitive science.
   b) Explain how this system might influence our understanding of mathematical concepts or language processing.

Ensure your response demonstrates a deep understanding of the mathematical operation, creativity in designing the linguistic representation, and the ability to apply the system to solve problems and draw broader connections."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a clear description of a linguistic transformation system for {t['operation']}.",
            "The system must accurately capture the essential properties of the mathematical operation.",
            "The response must include a complex expression represented using the designed system.",
            "The response must propose and solve a real-world problem using the linguistic representation system.",
            "The explanation should demonstrate a deep understanding of both mathematics and linguistics.",
            "The reflection should discuss implications for mathematics education or cognitive science."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
