class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem_description": "Design an algorithm to find the shortest path between two nodes in a graph. The graph is represented as an adjacency matrix, and the weights represent distances between nodes. The adjacency matrix is a 2D array where the value at index [i][j] represents the distance from node i to node j. If there is no direct path between nodes, the value is infinity."},
            "2": {"problem_description": "Design an algorithm to maximize the profit from a knapsack problem, where you have a set of items, each with a weight and a value, and a knapsack with a maximum weight capacity. The goal is to select a subset of items to maximize the total value without exceeding the weight capacity. Ensure your algorithm handles edge cases such as items with zero weight or zero value."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an algorithm to solve the following optimization problem:

Problem Description: {t['problem_description']}

Ensure that your algorithm is efficient, correct, and appropriately handles all edge cases. Provide a clear explanation of your approach, including the reasoning behind your chosen algorithm, its efficiency, and any assumptions made. Submit your algorithm as a plain text string in the following format:

Algorithm:
[Your algorithm here]

Explanation:
[Your explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The algorithm should be correct and solve the given optimization problem.",
            "The explanation should clearly describe the reasoning behind the chosen approach.",
            "The algorithm should be efficient, handle edge cases appropriately, and be clear and complete."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
