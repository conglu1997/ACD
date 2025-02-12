class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "spec": "Write a Python function called 'fibonacci' that takes an integer n and returns the nth Fibonacci number. Ensure the function handles invalid input (e.g., negative numbers) by returning None. The function should have a time complexity of O(n). Example inputs and outputs: fibonacci(5) -> 5, fibonacci(10) -> 55, fibonacci(-1) -> None."
            },
            "2": {
                "spec": "Write a Python function called 'is_prime' that takes an integer n and returns True if n is a prime number and False otherwise. Ensure the function handles invalid input (e.g., non-integer values) by returning None. The function should have a time complexity of O(sqrt(n)). Example inputs and outputs: is_prime(5) -> True, is_prime(10) -> False, is_prime('a') -> None."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a Python function based on the following specifications:

{t['spec']}

Ensure your function is correctly implemented, follows the given constraints, and handles invalid inputs appropriately. Your function should be efficient with the specified time complexity. Submit your function as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The function should handle invalid input appropriately.",
            "The function should meet the specified time complexity.",
            "The function should return the correct outputs for the given examples."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
