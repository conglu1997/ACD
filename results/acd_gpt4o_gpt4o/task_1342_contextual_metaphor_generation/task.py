class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"context": "business", "scenario": "Describe the market competition using a metaphor."},
            "2": {"context": "emotions", "scenario": "Explain the feeling of joy using a metaphor."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """Your task is to generate a metaphor based on the following context and scenario:

Context: {0}
Scenario: {1}

Ensure that your metaphor is creative, contextually appropriate, and clearly conveys the intended meaning. Provide your response in the following format:

Metaphor: [Your metaphor]

Example (different context):
Context: Weather
Scenario: Describe a storm using a metaphor.
Metaphor: The storm was a roaring lion, tearing through the trees with its fierce winds.

Your metaphor should be original and not a common cliché.""".format(t["context"], t["scenario"])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The metaphor should be creative and contextually appropriate, clearly conveying the intended meaning.",
            "The metaphor should be original and not a common cliché.",
            "The metaphor should be clear and understandable."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
