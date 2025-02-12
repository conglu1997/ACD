class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A manager tends to favor employees who share the same hobbies as him, often giving them better performance reviews compared to others who perform equally well but do not share his hobbies. This results in those favored employees getting promotions more frequently."
            },
            "2": {
                "scenario": "A person reads about a rare disease online and starts to believe they have symptoms of that disease, despite a doctor assuring them they are healthy. They continue to seek out more information online, becoming increasingly convinced of their condition."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Identify and explain the cognitive biases present in the following scenario:

Scenario: {t['scenario']}

Your explanation should include:
1. The name of the cognitive bias (or biases) present.
2. A brief description of the bias, explaining its general characteristics and effects.
3. A clear explanation of how the bias is exhibited in the scenario provided.

Ensure your explanation is detailed, logically structured, and accurately links the bias to the scenario. Submit your response as a plain text string in the following format:
- Bias Name: [Name of the bias]
- Description: [Description of the bias]
- Explanation: [How the bias is exhibited in the scenario]

Make sure to follow the specified format exactly and provide a comprehensive explanation."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should correctly identify the cognitive bias.",
            "The description of the bias should be accurate and concise.",
            "The explanation should clearly and logically link the bias to the scenario.",
            "The response should follow the specified format precisely.",
            "The explanation should be detailed, logically structured, and comprehensive."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
