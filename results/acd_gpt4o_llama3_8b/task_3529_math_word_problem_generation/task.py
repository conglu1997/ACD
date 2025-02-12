class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "linear equations", "constraints": ["include at least two variables", "context should involve shopping", "include at least one real-life item and its price"]},
            "2": {"concept": "probability", "constraints": ["include a real-life scenario", "use basic probability principles", "involve at least three different outcomes"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        concept = t["concept"]
        constraints = ', '.join(t["constraints"])
        return f"""Generate a detailed mathematical word problem based on the given concept and constraints:

Concept: {concept}
Constraints: {constraints}

Ensure that the word problem is clear, coherent, accurately reflects the specified concept and constraints, and is solvable. The problem should be original and not copied from existing resources. Submit your word problem as a plain text string in the following format:

Word Problem: [Your word problem here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The word problem should accurately reflect the given mathematical concept.", "The word problem should adhere to the specified constraints.", "The word problem should be clear, coherent, and solvable.", "The word problem should be original."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
