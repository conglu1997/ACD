class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n - 1)"},
            "2": {"description": "Implement a function that takes a list of integers and returns a new list with each integer squared."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "code" in t:
            return f"""Your task is to interpret the following piece of code and describe its functionality in plain text:\n\n{t["code"]}\n\nProvide a detailed explanation of what the code does, including the purpose of each part of the code and any relevant concepts it uses. Focus on clarity and completeness in your description."""
        elif "description" in t:
            return f"""Your task is to generate a piece of code based on the following description:\n\n{t["description"]}\n\nEnsure that the code is correct, efficient, and adheres to the given specifications. Provide the code in a standard format, with appropriate indentation and comments to explain the logic."""
        return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "code" in t:
            criteria = [
                "The response should describe the functionality of the code.",
                "The response should explain the purpose of each part of the code.",
                "The response should reference any relevant programming concepts.",
            ]
        elif "description" in t:
            criteria = [
                "The generated code should match the given description.",
                "The code should be correct and efficient.",
                "The code should include appropriate indentation and comments.",
            ]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
