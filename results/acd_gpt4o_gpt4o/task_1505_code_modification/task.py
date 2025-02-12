class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "code": "def add(a, b):\n    return a + b\n\ndef subtract(a, b):\n    return a - b\n\ndef multiply(a, b):\n    return a * b\n\ndef divide(a, b):\n    if b != 0:\n        return a / b\n    else:\n        return 'Cannot divide by zero'",
                "requirements": "Add error handling to the divide function to raise a ValueError with the message 'Division by zero is not allowed' instead of returning a string. Also, add a new function called 'power' that takes two arguments and returns the first argument raised to the power of the second argument."
            },
            "2": {
                "code": "def reverse_string(s):\n    return s[::-1]\n\ndef is_palindrome(s):\n    return s == s[::-1]",
                "requirements": "Modify the reverse_string function to handle an input that is not a string by raising a TypeError with the message 'Input must be a string'. Also, add a new function called 'capitalize_words' that takes a sentence as input and returns the sentence with the first letter of each word capitalized."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to modify the given code snippet to meet the specified requirements. Ensure the code remains functional and efficient.

Code snippet:
{t['code']}

Requirements:
{t['requirements']}

Make the necessary changes and provide the updated code in plain text format. Ensure your updated code is well-formatted and adheres to best practices."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The updated code should meet all specified requirements.",
            "The code should be functional and free of syntax errors.",
            "The code should handle edge cases as specified in the requirements.",
            "The code should maintain or improve efficiency.",
            "The code should be well-formatted and adhere to best practices."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
