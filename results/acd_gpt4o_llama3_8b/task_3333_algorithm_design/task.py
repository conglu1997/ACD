class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Design an algorithm to find the shortest path in a maze represented by a 2D grid. The grid contains cells that are either open (0) or blocked (1). The algorithm should return the shortest path from the start cell (top-left) to the end cell (bottom-right), or indicate if no path exists. The maze can have multiple paths and dead ends."
            },
            "2": {
                "problem": "Design an algorithm to sort a list of integers using the merge sort technique. The algorithm should return the sorted list. The list can contain duplicate values and negative numbers." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a procedural algorithm to solve the following problem. Your response should include:
1. A clear description of the problem.
2. A step-by-step algorithm to solve the problem.
3. Any assumptions made or edge cases considered.
4. The expected output based on a given example input.

Problem:
{t['problem']}

Example response format:
- Problem Description: Describe the problem clearly.
- Algorithm: Provide a step-by-step procedural algorithm.
- Assumptions and Edge Cases: List any assumptions made or edge cases considered.
- Example Input and Output: Provide an example input and the expected output based on the algorithm."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The problem description should accurately reflect the given problem.",
            "The algorithm should be logically sound and solve the problem.",
            "Any assumptions or edge cases should be reasonable and well-considered.",
            "The example input and output should be consistent with the algorithm."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
