class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Write a Rust function to calculate the factorial of a given number. The function should be named 'factorial' and take an unsigned integer as input. It should return the factorial of the number as an unsigned integer."},
            "2": {
                "problem": "Write a Rust function to check if a given string is a palindrome. The function should be named 'is_palindrome' and take a string slice as input. It should return a boolean indicating whether the string is a palindrome."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write a Rust function to solve the following problem and provide an explanation of the code:

Problem: {t['problem']}

Your code should be syntactically correct and function as expected. Include an explanation of how your code works and why you chose this approach. Submit your response as a plain text string in the following format:

Code: [Your Rust code]\nExplanation: [Your explanation of the code]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The code should be syntactically correct and function as expected.",
            "The explanation should clearly describe how the code works and why this approach was chosen."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
