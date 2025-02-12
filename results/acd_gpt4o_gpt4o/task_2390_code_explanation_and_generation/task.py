class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)", "generation_requirements": "Write a function that computes the nth Fibonacci number iteratively."},
            "2": {"code": "class Dog:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n\n    def bark(self):\n        return f'{self.name} says woof!'", "generation_requirements": "Write a class Cat with __init__ and meow methods, similar to the Dog class."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """Your task is to perform two actions based on the given code snippet.

1. Code Explanation: Explain the given piece of code in plain English. Make sure to cover what the code does, how it works, and any important aspects or details.

2. Code Generation: Based on the provided requirements, generate a new piece of code. Ensure that your code is functional and meets the specified requirements.

Here is the code snippet for this task:

{code}

Generation Requirements: {generation_requirements}

Provide your response in the following format:

1. Code Explanation: [Your detailed explanation here]
2. Code Generation: [Your generated code here]""".format(code=t["code"], generation_requirements=t["generation_requirements"])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should accurately describe the given code and cover all important aspects.", "The generated code should be functional and meet the specified requirements."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
