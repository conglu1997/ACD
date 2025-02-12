class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": "def fib(n):\n if n <= 1: return n\n else: return fib(n-1) + fib(n-2)"},
            "2": {"code": "def prime_factors(n):\n i = 2\n factors = []\n while i * i <= n:\n if n % i:\n i += 1\n else:\n n //= i\n factors.append(i)\n if n > 1:\n factors.append(n)\n return factors"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze and optimize the given code snippet for performance. Identify any inefficiencies in the code and rewrite it to improve its efficiency. Ensure that the optimized code retains the same functionality and correctness as the original code.

Code Snippet:
{t['code']}

Provide your optimized code in plain text format, along with a brief explanation of the changes you made and why they improve the performance.

Format your response as follows:
Optimized Code: [Your optimized code]
Explanation: [Explanation of the optimization]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The optimized code should improve performance compared to the original code.", "The optimized code should retain the same functionality and correctness as the original code.", "The explanation should clearly describe the changes made and their impact on performance."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
