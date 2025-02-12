class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Given an array of integers, return a new array where each element is the square of the original array's elements in non-decreasing order. Example: Input: [-4, -1, 0, 3, 10] Output: [0, 1, 9, 16, 100]"},
            "2": {"problem": "Write a function that takes a string and returns the string reversed, but with the order of words preserved. Example: Input: 'Hello World!' Output: 'olleH !dlroW'"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design a simple programming algorithm to solve the following problem:\n\nProblem Statement: {t['problem']}\n\nYour response should include:\n1. A clear and concise algorithm description.\n2. The corresponding code implementation in Python.\n\nEnsure that your algorithm is efficient and correctly solves the problem. Provide your response in plain text format without any additional formatting.\n\nExpected response format:\nAlgorithm Description: [Your algorithm description]\nPython Code: [Your Python code implementation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a clear and concise algorithm description.",
            "The response should include a correct and efficient code implementation in Python.",
            "The code should solve the given problem correctly.",
            "The response should follow the expected format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
