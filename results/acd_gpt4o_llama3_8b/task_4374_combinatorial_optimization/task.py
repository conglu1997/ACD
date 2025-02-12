class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Solve the Traveling Salesman Problem for the following set of cities with their pairwise distances: A-B: 10, A-C: 15, A-D: 20, B-C: 35, B-D: 25, C-D: 30. Return the shortest possible route that visits each city exactly once and returns to the starting city.",
                "answer": "N/A"
            },
            "2": {
                "problem": "Solve the 0/1 Knapsack Problem with the following items: \nItem 1: Weight = 2, Value = 3\nItem 2: Weight = 3, Value = 4\nItem 3: Weight = 4, Value = 5\nItem 4: Weight = 5, Value = 8\nThe knapsack has a maximum capacity of 5. Return the maximum value that can be obtained by selecting a subset of the items without exceeding the capacity.",
                "answer": "N/A"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following combinatorial optimization problem:

Problem:
{t['problem']}

Provide your solution as a plain text string, clearly indicating the optimal solution and the method used to find it. Your submission should be in the following format:

Solution: [Your Solution Here]
Method: [Description of the method used to find the solution]

Ensure that your solution is optimal and that the method is clearly explained. Verify that you understand the problem requirements before submitting your solution."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The solution should correctly solve the given combinatorial optimization problem.",
            "The method used to find the solution should be clearly explained.",
            "The solution should be optimal and correctly justified."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
