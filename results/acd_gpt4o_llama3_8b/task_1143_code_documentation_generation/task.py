class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "code": """def add(a, b):
    \"\"\"Add two numbers and return the result.\"\"\"
    return a + b

class Calculator:
    def __init__(self):
        self.result = 0

    def calculate(self, a, b, operation):
        \"\"\"Perform the given operation on two numbers.\"\"\"
        if operation == 'add':
            self.result = add(a, b)
        return self.result
"""
            },
            "2": {
                "code": """def factorial(n):
    \"\"\"Calculate the factorial of a number.\"\"\"
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

class MathUtils:
    def __init__(self):
        pass

    def compute_factorial(self, number):
        \"\"\"Compute the factorial of the given number.\"\"\"
        return factorial(number)
"""
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate comprehensive documentation for the following code snippet. Your documentation should include a brief description of each function and class, explanations of parameters and return values, and any additional details that help understand the code's functionality. Submit your documentation as a plain text string.\n\nCode:\n{t['code']}\n\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The documentation should clearly explain the purpose of each function and class.",
            "The parameters and return values should be described accurately.",
            "The documentation should be comprehensive and enhance the understanding of the code."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
