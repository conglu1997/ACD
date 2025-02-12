class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Write a Haskell function to calculate the nth Fibonacci number. The function should be named 'fibonacci' and take an integer as input. It should return the nth Fibonacci number as an integer."},
            "2": {"problem": "Write a Haskell function to check if a given list is a palindrome. The function should be named 'isPalindrome' and take a list of integers as input. It should return True if the list is a palindrome and False otherwise."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write a Haskell function to solve the following problem and provide an explanation of the code:

Problem: {t['problem']}

Your code should be syntactically correct and function as expected. Include an explanation of how your code works and why you chose this approach. Submit your response as a plain text string in the following format:

Code: [Your Haskell code]
Explanation: [Your explanation of the code]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The code should be syntactically correct and function as expected.", "The explanation should clearly describe how the code works and the approach taken."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
