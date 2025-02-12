class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "experiment": "measuring the density of a solid object using water displacement"
            },
            "2": {
                "experiment": "demonstrating Newton's second law of motion using a cart and weights"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Describe the steps and principles involved in conducting the following physics experiment:

Experiment: {t['experiment']}

Your description should include:
1. The materials needed
2. Detailed steps to perform the experiment
3. The underlying physical principles

Ensure that your explanation is clear, accurate, and logically organized. Submit your description as a plain text string.

Example response format:
Materials:
- List of materials
Steps:
1. Step one
2. Step two
Principles:
- Explanation of principles
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The description should include all necessary materials.",
            "The steps to perform the experiment should be detailed and clear.",
            "The underlying physical principles should be accurately explained.",
            "The explanation should be logically organized and easy to follow."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
