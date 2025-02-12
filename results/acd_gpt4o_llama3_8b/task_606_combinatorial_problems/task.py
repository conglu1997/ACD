class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "type": "permutation",
                "problem": "How many distinct ways can the letters in the word 'BINARY' be arranged?"
            },
            "2": {
                "type": "combination",
                "problem": "In how many ways can a committee of 3 people be formed from a group of 10 people?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'permutation':
            return f"""Solve the following combinatorial problem:

Problem: {t['problem']}

To solve this problem, consider the number of ways to arrange 6 unique letters. The formula to use is n! (n factorial), where n is the number of items to arrange. For example, if you have 3 letters, A, B, and C, the number of distinct arrangements is 3! = 6 (ABC, ACB, BAC, BCA, CAB, CBA).

Submit your answer as a plain text string in the format: [Answer]. Ensure your answer is a positive integer.
Example: 720"""
        else:
            return f"""Solve the following combinatorial problem:

Problem: {t['problem']}

To solve this problem, consider the number of ways to choose 3 people out of 10, which is given by the combination formula C(n, k) = n! / (k!(n-k)!), where n is the total number of items, and k is the number of items to choose. For example, if you have 5 people and you want to choose 2, the number of ways is C(5, 2) = 5! / (2!(5-2)!) = 10.

Submit your answer as a plain text string in the format: [Answer]. Ensure your answer is a positive integer.
Example: 120"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['type'] == 'permutation':
            validation_criteria = ["The response should correctly calculate the number of distinct ways to arrange the given letters."]
        else:
            validation_criteria = ["The response should correctly calculate the number of ways to form the committee using the combination formula."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
