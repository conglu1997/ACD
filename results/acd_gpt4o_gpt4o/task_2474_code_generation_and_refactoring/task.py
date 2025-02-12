class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task": "Write a Python function that takes a list of integers and returns a new list containing only the even numbers. The function should be implemented in a single line using list comprehension.",
                "constraints": "The function should be implemented in a single line using list comprehension."
            },
            "2": {
                "task": "Refactor the following Python function to improve its efficiency and readability. The function takes a list of integers and returns a new list with each element squared.",
                "code": "def square_elements(lst):\n    result = []\n    for i in lst:\n        result.append(i * i)\n    return result"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        task = t.get('task', '')
        constraints = t.get('constraints', '')
        code = t.get('code', '')
        instructions = f"""Your task is to complete the following programming task:

{task}

{constraints}

{code}

Ensure that your code adheres to the given constraints and is efficient and readable. Provide your solution in plain text format:

Solution:
[Your code here]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The code should adhere to the given constraints.",
            "The code should be efficient and readable.",
            "The code should accomplish the task as described."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
