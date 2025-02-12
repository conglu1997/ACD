class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "There are 3 boxes in a row. The first box contains a red ball, the second box contains a blue ball, and the third box is empty. Swap the positions of the red and blue balls such that the red ball is in the second box and the blue ball is in the first box. Describe the steps to achieve this."},
            "2": {"puzzle": "You have a 3x3 grid. Place the numbers 1 to 9 in the grid so that each row, column, and diagonal sums to 15. Describe the final arrangement of numbers in the grid."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        puzzle = t["puzzle"]
        return f"""Solve the following visual puzzle based on the given instructions:\n\n{puzzle}\n\nEnsure that your solution is clear, logically sound, and follows the instructions accurately. Provide your solution as a plain text string describing each step or the final arrangement as required. Avoid adding any unnecessary information that is not relevant to solving the puzzle.\n\nSubmit your response in the following format:\n1. Steps: [Your step-by-step solution here] or\n2. Final Arrangement: [Your final arrangement here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["puzzle"].startswith("There are 3 boxes in a row"):
            criteria = [
                "The steps should correctly swap the positions of the red and blue balls.",
                "The red ball should end up in the second box.",
                "The blue ball should end up in the first box."]
        else:
            criteria = [
                "The final arrangement should be a 3x3 grid.",
                "Each row, column, and diagonal should sum to 15."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
