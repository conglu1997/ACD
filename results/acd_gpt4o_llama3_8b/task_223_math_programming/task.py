class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Write a Python program to find all prime numbers less than 100. The program should output the primes as a list."
            },
            "2": {
                "problem": "Write a Python program to solve the Fibonacci sequence up to the 20th term. The program should output the sequence as a list."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write a Python program to solve the given mathematical problem:

Problem:
{t['problem']}

The program should be efficient and correctly implement the mathematical solution. Submit your response as a plain text string containing the Python code."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The program should correctly solve the problem.",
            "The program should be written in Python.",
            "The output should be correct as specified in the problem statement."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
