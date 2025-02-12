class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"constraints": ["The puzzle must involve a 4x4 grid of numbers.", "Each row and column must contain unique numbers from 1 to 4.", "The solution must be unique.", "Provide the initial state with at least 4 numbers filled in."]},
            "2": {"constraints": ["The puzzle must involve a series of five logic statements.", "The solution must be deducible from the given statements.", "The statements must be clear and unambiguous.", "The solution must involve at least four variables."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        constraints = '\n'.join(t["constraints"])
        return f"""Generate a logical puzzle based on the following constraints:\n\n{constraints}\n\nEnsure that the puzzle is challenging yet solvable, and that the solution is unique. Provide the puzzle and its solution as a plain text string in the following format: \nPuzzle: [your puzzle here]\nSolution: [your solution here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The puzzle must adhere to all given constraints.",
            "The puzzle must be challenging yet solvable.",
            "The solution must be unique."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
