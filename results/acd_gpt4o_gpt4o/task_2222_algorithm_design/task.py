class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Design an algorithm to sort a list of integers in ascending order. Optimize for time complexity.",
                "data": [5, 2, 9, 1, 5, 6]},
            "2": {
                "problem": "Design an algorithm to find the shortest path between two nodes in a graph. Optimize for both time and space complexity.",
                "data": {"graph": {"A": {"B": 1, "C": 4}, "B": {"C": 2, "D": 5}, "C": {"D": 1}, "D": {}}, "start": "A", "end": "D"}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design an algorithm based on the following problem statement:

Problem:
{t['problem']}

Data:
{t['data']}

Ensure that your algorithm is efficient and optimized for the specified criteria. Submit your response as a Python code snippet that implements the algorithm. Your Python code should include test cases to demonstrate the correctness and efficiency of your algorithm."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The submission should correctly implement the algorithm based on the problem statement.",
                   "The algorithm should be optimized for the specified criteria (e.g., time complexity, space complexity).",
                   "The submission should include test cases demonstrating the correctness and efficiency of the algorithm."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
