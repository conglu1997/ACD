class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task": "modify_code",
                "code": "def greet(name):\n    return f'Hello, {name}!'\n\nprint(greet('World'))",
                "requirements": "Modify the function to accept an additional argument 'greeting' and use it instead of 'Hello'."
            },
            "2": {
                "task": "comprehend_code",
                "code": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)\n\nprint(factorial(5))",
                "question": "What does this code do? Provide a detailed explanation."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task'] == 'modify_code':
            return f"You are given the following piece of code:\n\n{t['code']}\n\nYour task is to modify this code based on the following requirement: {t['requirements']}\n\nSubmit your modified code as a plain text string in the following format:\n\n'Code: [Your modified code]'\n"
        elif t['task'] == 'comprehend_code':
            return f"You are given the following piece of code:\n\n{t['code']}\n\nYour task is to comprehend what this code does and provide a detailed explanation. Submit your explanation as a plain text string in the following format:\n\n'Explanation: [Your detailed explanation]'\n"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task'] == 'modify_code':
            validation_criteria = [
                "The modified function should accept an additional argument 'greeting'.",
                "The modified function should use the 'greeting' argument instead of 'Hello'.",
                "The modified code should be syntactically correct and runnable."
            ]
        elif t['task'] == 'comprehend_code':
            validation_criteria = [
                "The explanation should correctly describe the code's functionality.",
                "The explanation should be detailed and clear."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
