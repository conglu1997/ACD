class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "code_snippet": "def factorial(n):\n    if n == 0 or n == 1:\n        return 1\n    else:\n        return n * factorial(n-1)",
                "question": "What is the purpose of the given code snippet?"
            },
            "2": {
                "specification": "Write a Python function that takes a list of integers and returns a new list with only the even numbers from the original list."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "code_snippet" in t:
            return f"""Your task is to read and understand the following code snippet and answer the question provided.\n\nCode Snippet:\n{t['code_snippet']}\n\nQuestion:\n{t['question']}\n\nProvide your answer in plain text format."""
        elif "specification" in t:
            return f"""Your task is to write a Python function that meets the following specification:\n\nSpecification:\n{t['specification']}\n\nProvide your function in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "code_snippet" in t:
            criteria = ["The response should accurately describe the purpose of the code snippet."]
        else:
            criteria = ["The function should correctly filter out even numbers from a list of integers."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
