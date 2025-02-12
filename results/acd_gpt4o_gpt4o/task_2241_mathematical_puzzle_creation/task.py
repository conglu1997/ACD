class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "algebra", "constraints": "The puzzle should involve quadratic equations with real coefficients and have a unique real solution. Include all necessary steps and explanations to solve the equation."},
            "2": {"type": "geometry", "constraints": "The problem should involve calculating the area of a complex shape that is composed of at least three different basic geometric figures. Include all necessary steps, formulas, and explanations used to calculate the area."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem_type = t["type"]
        constraints = t["constraints"]
        instructions = f"""Your task is to create a novel mathematical puzzle or problem of the following type:

Type: {problem_type}

Constraints: {constraints}

Provide a detailed description of the puzzle or problem, including all necessary information and constraints. Then, solve the problem and provide a detailed explanation of the solution. Ensure that your puzzle is original, clear, and meets the given constraints. Provide your response in plain text format with the following structure:

1. Puzzle Description: [Your detailed description here]
2. Solution: [Your detailed solution here]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The puzzle should be original and meet the given constraints.",
            "The problem should be clearly described and solvable.",
            "The solution should be correct, well-explained, and include all necessary steps and explanations."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
