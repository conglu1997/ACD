class TaskFamily:
    from itertools import combinations, permutations

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "constraints": "Create a puzzle where the solution is a 4-digit number, each digit is unique, and the sum of the digits is 20."
            },
            "2": {
                "puzzle": "Find all unique 3-letter combinations from the set {A, B, C, D, E} where no letter repeats and the letters are in alphabetical order."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "constraints" in t:
            return (
                "Your task is to create a combinatorial puzzle based on the given constraints. "
                "Ensure that the puzzle is logically sound and has a unique solution. "
                "Provide the puzzle in the following format:\n\n"
                "1. Description of the puzzle\n"
                "2. Constraints\n"
                "3. Unique solution\n\n"
                "Example Response:\n"
                "1. Description of the puzzle: Create a 4-digit number where each digit is unique and the sum is 20.\n"
                "2. Constraints: Each digit must be unique and the sum must be 20.\n"
                "3. Unique solution: 5834"
            )
        elif "puzzle" in t:
            return (
                "Your task is to solve the provided combinatorial puzzle. "
                "Provide the solution in the following format:\n\n"
                "1. Solution\n"
                "2. Explanation of reasoning\n\n"
                "Example Response:\n"
                "1. Solution: ABC, ABD, ABE, ACD, ACE, ADE, BCD, BCE, BDE, CDE\n"
                "2. Explanation of reasoning: Listed all combinations of 3 unique letters from the set {A, B, C, D, E} in alphabetical order."
            )
        return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "constraints" in t:
            criteria = [
                "The puzzle must adhere to the given constraints.",
                "The puzzle must be logically sound and solvable.",
                "The puzzle must have a unique solution.",
                "The response format must follow the specified structure."
            ]
        elif "puzzle" in t:
            criteria = [
                "The solution must correctly solve the provided puzzle.",
                "The explanation must demonstrate logical reasoning.",
                "The response format must follow the specified structure."
            ]
        else:
            return 0.0
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
