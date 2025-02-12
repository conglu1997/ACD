class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Sort a list of integers using a custom sorting rule.", "constraints": "The sorting rule should prioritize even numbers over odd numbers and within each parity, numbers should be sorted in ascending order."},
            "2": {"problem": "Design an algorithm to find the longest common subsequence in two strings.", "constraints": "The algorithm should be efficient and its time complexity should not exceed O(m*n), where m and n are the lengths of the two strings."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design an algorithm to solve the following problem based on the specified constraints. Describe the algorithm in detail and explain the rationale behind your design choices. Ensure that the algorithm meets the given constraints and is efficient.

Problem: {t['problem']}
Constraints: {t['constraints']}

Provide your response in the following format:
Algorithm: <Your algorithm description>
Rationale: <Your explanation>"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The algorithm should meet the specified constraints.",
            "The rationale should clearly explain the design choices and efficiency of the algorithm."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
