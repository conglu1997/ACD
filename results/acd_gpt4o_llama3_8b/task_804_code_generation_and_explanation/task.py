class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Write a Python function that takes a list of integers and returns a new list containing only the prime numbers from the original list. The function should handle lists of up to 100,000 integers efficiently."
            },
            "2": {
                "problem": "Write a Python function that takes a string and returns the longest substring without repeating characters. The function should handle strings of up to 1,000 characters efficiently."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a Python function to solve the given problem and explain how your code works.

Problem: {t['problem']}

Your response should include:
1. The Python function solving the problem.
2. An explanation of how the code works, including the logic and any key steps.

Submit your response as a plain text string in the following format:
- Code: [Your code here]
- Explanation: [Your explanation here]

Make sure to follow the specified format exactly and provide a comprehensive explanation."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The code should correctly solve the given problem.",
            "The explanation should clearly describe how the code works, including the logic and key steps.",
            "The response should follow the specified format precisely.",
            "The code should be syntactically correct and executable.",
            "The explanation should be coherent and logically structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
