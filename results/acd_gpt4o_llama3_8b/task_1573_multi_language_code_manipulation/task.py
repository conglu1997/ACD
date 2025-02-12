class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "language": "Python",
                "code_snippet": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)",
                "modification": "Modify the function to use an iterative approach instead of recursion."
            },
            "2": {
                "language": "JavaScript",
                "code_snippet": "function greet(name) {\n    return 'Hello, ' + name + '!';\n}",
                "modification": "Modify the function to use template literals for string concatenation and ensure it handles null or undefined input gracefully by returning 'Hello, Guest!'."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given a code snippet written in {t['language']}. Your task is to modify the code based on the given requirement. Ensure that the modified code is syntactically correct and meets the specified requirement. Submit your response as a plain text string with the modified code.

Code Snippet:
{t['code_snippet']}

Modification Requirement:
{t['modification']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The modified code should be syntactically correct.",
            "The modified code should meet the specified requirement."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
