class TaskFamily:
    import sys
    import traceback

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Given an unsorted array of integers, find the length of the longest consecutive elements sequence."
            },
            "2": {
                "problem": "Design an algorithm to find the lowest common ancestor of two nodes in a binary tree. Each node contains a reference to its parent."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given the following problem: {t['problem']}

Design an algorithm to solve this problem. Ensure that your solution is correct and efficient. Provide a detailed explanation of your approach, including the time and space complexity. Your explanation should be clear and comprehensive enough for someone with a basic understanding of algorithms to follow.

Submit your response as a plain text string in the following format:

Algorithm:
[Your algorithm in plain text or pseudocode]

Explanation:
[Your detailed explanation]

Example Format:
Algorithm:
1. Store all elements in a data structure that allows O(1) lookups.
2. Iterate through the array to find the start of a sequence.
3. Count the length of the sequence by checking consecutive elements.

Explanation:
First, store all elements in a hash set to allow O(1) lookups. Then, iterate through the array. For each element, check if it is the start of a sequence by verifying if the previous element is not in the set. If it is the start, count the length of the sequence by checking consecutive elements in the set. This ensures an overall time complexity of O(n) and space complexity of O(n)."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        try:
            from src.eval_helper import eval_with_llm_judge
            instructions = TaskFamily.get_instructions(t)
            criteria = [
                "The algorithm must solve the given problem correctly.",
                "The explanation must be detailed and clear.",
                "The time and space complexity of the algorithm must be provided.",
                "The solution must be efficient considering the problem constraints."
            ]
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
        except Exception as e:
            print(f"Exception during scoring: {str(e)}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            return 0.0
