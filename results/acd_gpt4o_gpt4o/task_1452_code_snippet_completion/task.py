class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Complete the function to check if a number is prime.", "code": "def is_prime(n):\n    # Your code here\n    pass"},
            "2": {"description": "Complete the function to find the nth Fibonacci number using recursion.", "code": "def fibonacci(n):\n    # Your code here\n    pass"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to complete the following code snippet to achieve the specified functionality:\n\nDescription: {t['description']}\n\nCode:\n{t['code']}\n\nProvide your solution by filling in the 'Your code here' part. The function should be implemented such that it returns the correct result for any valid input. Do not include any print statements in your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        try:
            # Create a local namespace to execute the submission
            local_namespace = {}
            exec(submission, {}, local_namespace)

            if t['description'] == "Complete the function to check if a number is prime.":
                # Check the is_prime function
                is_prime = local_namespace.get('is_prime')
                if not is_prime:
                    return 0.0
                test_cases = [(2, True), (4, False), (17, True), (20, False), (31, True), (1, False), (0, False), (-5, False), (97, True), (100, False)]
                return 1.0 if all(is_prime(n) == expected for n, expected in test_cases) else 0.0

            elif t['description'] == "Complete the function to find the nth Fibonacci number using recursion.":
                # Check the fibonacci function
                fibonacci = local_namespace.get('fibonacci')
                if not fibonacci:
                    return 0.0
                test_cases = [(0, 0), (1, 1), (5, 5), (10, 55), (15, 610), (20, 6765), (25, 75025), (2, 1), (3, 2), (4, 3)]
                return 1.0 if all(fibonacci(n) == expected for n, expected in test_cases) else 0.0

            return 0.0
        except Exception as e:
            return 0.0
