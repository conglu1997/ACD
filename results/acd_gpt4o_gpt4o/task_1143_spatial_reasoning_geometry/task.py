class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"shape": "triangle", "properties": {"sides": [3, 4, 5], "angles": []}, "question": "What is the area of this triangle?", "expected_result": "6"},
            "2": {"shape": "rectangle", "properties": {"sides": [5, 10]}, "question": "What is the perimeter of this rectangle?", "expected_result": "30"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["shape"] == "triangle":
            return f"""Solve the following problem involving a triangle:

Properties: Sides: {t["properties"]["sides"]}

Question: {t["question"]}

Provide your answer in plain text format. Ensure your answer is a single number representing the area of the triangle."""
        elif t["shape"] == "rectangle":
            return f"""Solve the following problem involving a rectangle:

Properties: Sides: {t["properties"]["sides"]}

Question: {t["question"]}

Provide your answer in plain text format. Ensure your answer is a single number representing the perimeter of the rectangle."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [f"The response should match the expected result: {t['expected_result']}."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
