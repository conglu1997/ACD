class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Design an algorithm to find the greatest common divisor (GCD) of two integers using the Euclidean algorithm. Optimize the algorithm for efficiency and explain why the optimization works."},
            "2": {"problem": "Design an algorithm to sort a list of integers using the quicksort algorithm. Optimize the algorithm for efficiency and explain the choice of pivot selection."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        return f"""Design and optimize an algorithm based on the given problem:

Problem: {problem}

Provide your solution with the following elements:
1. A detailed explanation of the algorithm.
2. The optimized code implementation in Python.
3. An explanation of why the optimization works.

Submit your solution as a plain text string in the following format:

Explanation: [Detailed explanation of the algorithm]
Code: [Optimized Python code]
Optimization Explanation: [Explanation of why the optimization works]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should be detailed and clear.",
            "The code should be correct and optimized.",
            "The optimization explanation should be logical and valid."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
