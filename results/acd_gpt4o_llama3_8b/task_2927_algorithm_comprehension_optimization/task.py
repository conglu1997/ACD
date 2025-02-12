class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "algorithm": "Bubble Sort",
                "description": "Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted."
            },
            "2": {
                "algorithm": "Dijkstra's Algorithm",
                "description": "Dijkstra's Algorithm is used to find the shortest path between nodes in a graph. It works by iteratively selecting the node with the smallest known distance, updating the distances of neighboring nodes, and marking the selected node as 'visited'."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Understand the given algorithm and propose optimizations or improvements. Provide a clear explanation of the original algorithm, your proposed changes, and the reasoning behind them. Ensure your explanation covers the following aspects:

1. Overview of the original algorithm.
2. Identification of potential inefficiencies or limitations.
3. Detailed description of proposed optimizations or improvements.
4. Explanation of how the optimizations improve the algorithm's performance or address its limitations.

Algorithm: {t['algorithm']}
Description: {t['description']}

Submit your response as a plain text string in the following format:

Original Algorithm:
[Overview of the original algorithm]

Proposed Optimizations:
[Description of proposed optimizations]

Reasoning:
[Explanation of how the optimizations improve the algorithm]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should clearly describe the original algorithm.",
            "The proposed optimizations should be logically sound and feasible.",
            "The reasoning should convincingly explain how the optimizations improve the algorithm."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
