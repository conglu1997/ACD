class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "puzzle": "Determine the area of a regular hexagon with a side length of 6 units.",
                "step_by_step_solution": "Calculate the area of one of the six equilateral triangles that make up the hexagon and sum them up.",
                "solution": "The area of a regular hexagon with a side length of 6 units is 93.53 square units."
            },
            "2": {
                "puzzle": "Find the length of the diagonal of a rectangle with a length of 8 units and a width of 6 units.",
                "step_by_step_solution": "Use the Pythagorean theorem to determine the length of the diagonal.",
                "solution": "The length of the diagonal of the rectangle is 10 units."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following geometric puzzle and provide a step-by-step solution. Include explanations of the geometric principles used in your solution. If necessary, describe any diagrams textually.

Puzzle: {t['puzzle']}

Submit your solution as a plain text string, including step-by-step explanations and textual descriptions of any diagrams. Your solution should follow this format:

1. Step-by-step solution: [Your detailed solution here]
2. Explanation of geometric principles: [Your explanation here]
3. Diagram description (if any): [Your text description of the diagram here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should be correct and match the provided answer.",
            "The step-by-step explanation should be clear and logically consistent.",
            "Any geometric principles used should be correctly explained.",
            "The solution should be presented in the required format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
