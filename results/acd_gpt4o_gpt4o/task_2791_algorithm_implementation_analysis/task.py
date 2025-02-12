class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"algorithm": "Implement the Quick Sort algorithm and analyze its time complexity.", "input": [3, 6, 8, 10, 1, 2, 1]},
            "2": {"algorithm": "Implement Dijkstra's algorithm for finding the shortest path in a graph and analyze its space complexity.", "graph": {"A": {"B": 1, "C": 4}, "B": {"C": 2, "D": 5}, "C": {"D": 1}, "D": {}}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'input' in t:
            return f"""Your task is to implement the following algorithm and analyze its complexity.

Algorithm:
{t['algorithm']}

Input:
{t['input']}

Instructions:
1. Implement the algorithm in Python.
2. Provide a detailed analysis of its time complexity.
3. Ensure your implementation is correct and well-documented.
4. Use the provided input to test your implementation and include the output in your response.

Format your response as follows:

Implementation:
[Your Python code]

Output:
[Result of running your code with the provided input]

Complexity Analysis:
[Your analysis]
"""
        else:
            return f"""Your task is to implement the following algorithm and analyze its complexity.

Algorithm:
{t['algorithm']}

Graph:
{t['graph']}

Instructions:
1. Implement the algorithm in Python.
2. Provide a detailed analysis of its space complexity.
3. Ensure your implementation is correct and well-documented.
4. Use the provided graph to test your implementation and include the output in your response.

Format your response as follows:

Implementation:
[Your Python code]

Output:
[Result of running your code with the provided graph]

Complexity Analysis:
[Your analysis]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The algorithm implementation must be correct and functional.",
            "The complexity analysis must be accurate and detailed.",
            "The code must be well-documented and readable.",
            "The provided output must match the expected results for the given input or graph."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
