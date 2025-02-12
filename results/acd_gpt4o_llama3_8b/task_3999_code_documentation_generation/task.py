class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "code": """def fibonacci(n):\n    '''\n    Generate the nth Fibonacci number.\n    :param n: The position of the Fibonacci number to generate.\n    :return: The nth Fibonacci number.\n    '''\n    if n <= 0:\n        return 0\n    elif n == 1:\n        return 1\n    else:\n        return fibonacci(n-1) + fibonacci(n-2)"""
            },
            "2": {
                "code": """class Queue:\n    def __init__(self):\n        self.items = []\n\n    def is_empty(self):\n        '''\n        Check if the queue is empty.\n        :return: True if the queue is empty, False otherwise.\n        '''\n        return len(self.items) == 0\n\n    def enqueue(self, item):\n        '''\n        Add an item to the queue.\n        :param item: Item to add.\n        '''\n        self.items.insert(0, item)\n\n    def dequeue(self):\n        '''\n        Remove an item from the queue.\n        :return: The item removed from the queue.\n        '''\n        return self.items.pop()\n\n    def size(self):\n        '''\n        Return the size of the queue.\n        :return: The number of items in the queue.\n        '''\n        return len(self.items)"""
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate user-friendly documentation for the following piece of code. Your documentation should include the following sections:\n\n1. Purpose: Explain the purpose of the code.\n2. Functionality: Describe what the code does and how it works.\n3. Usage: Provide instructions on how to use the code, including any relevant examples.\n\nCode:\n{t['code']}\n\nSubmit your documentation as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The documentation should include a 'Purpose' section explaining the purpose of the code.", "The documentation should include a 'Functionality' section describing what the code does and how it works.", "The documentation should include a 'Usage' section providing instructions on how to use the code, including any relevant examples.", "The documentation should be clear, concise, and comprehensible."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
