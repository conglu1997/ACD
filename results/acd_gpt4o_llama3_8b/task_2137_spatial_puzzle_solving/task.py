class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "pattern", "puzzle": "2, 5, 10, 17, ?"},
            "2": {"type": "shape_matching", "puzzle": "▲, ▲▲, ▲▲▲, ?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "pattern":
            return f"""Given the following numerical pattern, identify the next number in the sequence. Ensure that your answer is based on a logical and consistent pattern. Provide a brief explanation of the pattern you identified.

Pattern: {t['puzzle']}

Submit your response as a plain text string in the following format:
Next number: [Your answer]
Explanation: [Your explanation]"""
        elif t["type"] == "shape_matching":
            return f"""Given the following series of shapes, identify the next shape that completes the series. Ensure that your answer is based on a logical and consistent pattern. Provide a brief explanation of the pattern you identified.

Series: {t['puzzle']}

Submit your response as a plain text string in the following format:
Next shape: [Your answer]
Explanation: [Your explanation]"""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "pattern":
            criteria = ["The answer should be the next logical number in the given pattern.", "The explanation should logically justify the identified pattern."]
        elif t["type"] == "shape_matching":
            criteria = ["The answer should be the next logical shape in the given series.", "The explanation should logically justify the identified pattern."]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
