class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A person believes they are less likely to get into a car accident than the average driver despite statistics showing most people think this way.", "bias": ""},
            "2": {"scenario": "A manager continues to invest in a failing project because they have already spent a considerable amount of money on it.", "bias": ""}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Identify the cognitive bias in the following scenario and explain why it represents a bias. Your response should include the name of the bias and a detailed explanation:

Scenario: {t['scenario']}

Response format:
Bias Name: [Name of the cognitive bias]
Explanation: [Detailed explanation]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should correctly identify the cognitive bias.",
            "The response should provide a clear explanation of why the scenario represents a cognitive bias.",
            "The explanation should be detailed and well-reasoned.",
            "The response should be in plain text format.",
            "The response should follow the specified format: Bias Name: [Name of the cognitive bias] Explanation: [Detailed explanation]."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
