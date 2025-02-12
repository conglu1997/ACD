class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Sort an array of integers in ascending order using a sorting algorithm of your choice."},
            "2": {"problem": "Find the shortest path between two nodes in an unweighted graph."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        instructions = f"""Your task is to design an algorithm to solve the following problem:

{problem}

In addition to providing the algorithm, you must also include a clear explanation of how the algorithm works and why it is effective for solving the problem. Ensure that your explanation is detailed and covers the main steps of the algorithm.

Please provide your response in the following format:

Algorithm:
[Your algorithm here]

Explanation:
[Your explanation here]

Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The algorithm should correctly solve the given problem.",
            "The explanation should be clear and detailed, covering the main steps of the algorithm.",
            "The explanation should justify why the algorithm is effective for solving the problem."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
