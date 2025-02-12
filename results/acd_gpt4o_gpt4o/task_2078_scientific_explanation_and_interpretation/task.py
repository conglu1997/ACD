class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"phenomenon": "Photosynthesis in plants", "data": "[Time: 0, CO2 Level: 400 ppm, O2 Level: 21%], [Time: 1, CO2 Level: 390 ppm, O2 Level: 21.5%], [Time: 2, CO2 Level: 380 ppm, O2 Level: 22%], [Time: 3, CO2 Level: 370 ppm, O2 Level: 22.5%]"},
            "2": {"phenomenon": "Newton's Third Law of Motion", "data": "[Action: 10 N force applied to the right, Reaction: 10 N force to the left], [Action: 15 N force applied to the left, Reaction: 15 N force to the right], [Action: 20 N force applied to the right, Reaction: 20 N force to the left]"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves two parts: explanation and interpretation.

Part 1: Explanation
Explain the following scientific phenomenon in clear and concise terms:

Phenomenon: {t['phenomenon']}

Ensure your explanation is accurate and covers the key aspects of the phenomenon. Provide your response in plain text format.

Part 2: Interpretation
Interpret the provided scientific data related to the phenomenon. Describe what the data indicates and how it relates to the phenomenon explained in Part 1.

Data: {t['data']}

Ensure your interpretation is clear, logical, and accurately reflects the data. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should be accurate and cover the key aspects of the phenomenon.",
            "The interpretation should accurately reflect the data provided.",
            "The response should be clear, logical, and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
