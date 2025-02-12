class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "What is the next number in the sequence: 3, 9, 27, 81, ?"},
            "2": {"criteria": "Generate a mathematical puzzle that involves finding the next number in a sequence. Ensure the sequence follows a clear mathematical pattern."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "puzzle" in t:
            return f"""Solve the following mathematical puzzle: {t['puzzle']}

Provide your answer in plain text format."""
        elif "criteria" in t:
            return f"""Generate a mathematical puzzle based on the following criteria: {t['criteria']}

Ensure the puzzle is logical, follows a clear mathematical pattern, and is solvable. Provide your puzzle in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []

        if "puzzle" in t:
            expected_answer = "243"
            criteria.append(f"The response should be the number: {expected_answer}.")
        elif "criteria" in t:
            criteria.append("The response should be a logical, solvable mathematical puzzle involving a sequence and following a clear mathematical pattern.")

        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0