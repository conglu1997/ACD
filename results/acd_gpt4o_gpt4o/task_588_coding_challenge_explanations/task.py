class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Write a function named 'func' that takes a list of integers and returns the list sorted in ascending order."},
            "2": {"problem": "Write a function named 'func' that takes a string and returns the string with reversed words, but the words themselves remain in the original order."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to solve the following coding challenge and provide a detailed explanation of your solution.

Problem: {t['problem']}

Ensure your code is correct and your explanation is clear and covers all aspects of the solution logic. Your function must be named 'func'. Provide your response in plain text format structured as follows:

Code: [Your code]
Explanation: [Your explanation]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        import re
        from src.eval_helper import eval_with_llm_judge

        def extract_code_and_explanation(submission: str) -> tuple[str, str]:
            match = re.search(r"Code: (.*)Explanation: (.*)", submission, re.DOTALL)
            if match:
                return match.group(1).strip(), match.group(2).strip()
            return "", ""

        instructions = TaskFamily.get_instructions(t)
        code, explanation = extract_code_and_explanation(submission)

        # Define a helper function to test the code
        def test_code(problem: str, code: str) -> bool:
            try:
                exec_globals = {}
                exec(code, exec_globals)
                if problem == "Write a function named 'func' that takes a list of integers and returns the list sorted in ascending order.":
                    test_func = exec_globals.get('func')
                    return (test_func([3, 1, 2]) == [1, 2, 3] and
                            test_func([5, 3, 8, 1]) == [1, 3, 5, 8] and
                            test_func([1, 2, 3]) == [1, 2, 3] and
                            test_func([]) == [] and
                            test_func([-1, -3, -2]) == [-3, -2, -1])
                elif problem == "Write a function named 'func' that takes a string and returns the string with reversed words, but the words themselves remain in the original order.":
                    test_func = exec_globals.get('func')
                    return (test_func("Hello world") == "olleH dlrow" and
                            test_func("OpenAI GPT") == "IAnepO TPG" and
                            test_func("a b c") == "a b c" and
                            test_func("") == "" and
                            test_func("single") == "elgnis")
            except Exception:
                return False
            return False

        # Evaluate the code
        code_correct = test_code(t['problem'], code)
        # Evaluate the explanation with LLM judge
        criteria = ["The explanation should be clear and cover all aspects of the solution logic.",
                    "The explanation should detail how the code solves the problem step-by-step.",
                    "The explanation should mention edge cases handled by the code."]
        explanation_correct = eval_with_llm_judge(instructions, explanation, criteria)

        return 1.0 if code_correct and explanation_correct else 0.0
