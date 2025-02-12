class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code_snippet": "def add(a, b):\n    return a + b", "problem": "Create a function 'multiply' that multiplies two numbers using repeated addition.", "example_input": "print(multiply(3, 4))", "expected_output": "12"},
            "2": {"code_snippet": "def reverse_list(lst):\n    return lst[::-1]", "problem": "Create a function 'is_palindrome' that checks if a list is a palindrome.", "example_input": "print(is_palindrome([1, 2, 3, 2, 1]))", "expected_output": "True"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        code_snippet = t["code_snippet"]
        problem = t["problem"]
        example_input = t["example_input"]
        expected_output = t["expected_output"]
        instructions = f"""Your task is to read the following code snippet and generate a new function based on the given problem.\n\nCode Snippet:\n{code_snippet}\n\nProblem: {problem}\n\nExample Input: {example_input}\nExpected Output: {expected_output}\n\nEnsure that your function is correctly implemented and works as expected. Provide your response in plain text format.\n\nResponse format:\n\n<Your function definition>\n\nExample usage:\n{example_input}\nExpected output:\n{expected_output}"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The function should correctly solve the problem as described in the instructions.", "The function should produce the expected output for the given example input."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
