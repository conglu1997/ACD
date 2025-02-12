class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"pattern_sequence": "A, B, A, C, A, B, C, A, ?, ?"},
            "2": {"pattern_sequence": "1, 4, 9, 16, 25, 36, 49, ?, ?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        pattern_sequence = t["pattern_sequence"]
        return f"""Identify the pattern in the following sequence and provide the next two elements to complete it:

Pattern Sequence: {pattern_sequence}

Submit your response as a plain text string with the two elements separated by a comma. Example: element1, element2"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submission should correctly identify the pattern and provide the next two elements in the sequence.",
            "The response should be in the format: element1, element2."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
