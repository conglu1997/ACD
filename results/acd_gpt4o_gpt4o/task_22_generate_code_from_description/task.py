class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Write a Python function named 'fizzbuzz' that takes an integer 'n' and returns a list of strings representing the numbers from 1 to n. For multiples of three, it should return 'Fizz' instead of the number, and for the multiples of five, it should return 'Buzz'. For numbers which are multiples of both three and five, it should return 'FizzBuzz'."},
            "2": {"description": "Write a Python function named 'prime_numbers' that takes an integer 'n' and returns a list of all prime numbers less than or equal to 'n'."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        instructions = f"""Your task is to write a Python function based on the following description:

{description}

Function Signature:
For Task 1: def fizzbuzz(n: int) -> list[str]
For Task 2: def prime_numbers(n: int) -> list[int]

Provide the function definition in plain text format without any additional explanations."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The function should be syntactically correct.",
            "The function should meet the requirements specified in the description.",
            "The function should handle edge cases appropriately."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
