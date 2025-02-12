class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "You have a square piece of paper. Fold it in half to form a rectangle, then fold it in half again to form a smaller square. How many layers of paper are there now?"},
            "2": {"puzzle": "Imagine a cube with a side length of 3 units. If you paint the entire surface of the cube and then cut it into 1-unit cubes, how many of the smaller cubes will have paint on exactly one face?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        puzzle = t["puzzle"]
        instructions = f"""Your task is to solve the following spatial reasoning puzzle:

Puzzle: {puzzle}

Your solution should include the following elements:
1. A clear explanation of each step needed to solve the puzzle.
2. Any diagrams or visualizations that help explain your reasoning (optional but encouraged).
3. The final answer.

Provide your solution in the following format:

Step-by-step Explanation:
[Your explanation of each step]

Diagrams/Visualizations (if any):
[Your diagrams or visualizations]

Final Answer:
[Your final answer]

Ensure your response is clear and detailed."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should include each step needed to solve the puzzle.",
            "Any provided diagrams or visualizations should be correct and relevant.",
            "The final answer should be correct and clearly stated."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
