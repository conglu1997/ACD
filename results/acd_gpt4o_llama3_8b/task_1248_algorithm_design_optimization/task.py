class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'problem': 'Sort a list of integers in ascending order. The list contains 10,000 randomly generated integers. Your algorithm should be efficient in terms of time complexity.'
            },
            '2': {
                'problem': 'Design an algorithm to find the shortest path in a graph represented by an adjacency matrix. The graph contains 100 nodes and edges with random weights.'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an algorithm to solve the following computational problem:

Problem: {t['problem']}

Your response should include:
1. A description of the algorithm.
2. The pseudocode of the algorithm.
3. An explanation of why this algorithm is efficient, including its time complexity.

Ensure your algorithm is clear, logically sound, and optimized for efficiency. Submit your response as a plain text string in the following format:

Description: [Your description]
Pseudocode: [Your pseudocode]
Efficiency Explanation: [Your explanation, including time complexity]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            'The response must include a description, pseudocode, and efficiency explanation.',
            'The algorithm should logically solve the problem.',
            'The algorithm should be optimized for efficiency.',
            'The time complexity explanation should be accurate.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
