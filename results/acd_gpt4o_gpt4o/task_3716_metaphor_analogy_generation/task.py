class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "time", "context": "a fleeting moment"},
            "2": {"concept": "knowledge", "context": "a growing tree"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a metaphor or analogy based on the following concept and context:

Concept: {t['concept']}
Context: {t['context']}

Provide a metaphor or analogy that creatively and appropriately represents the given concept in the provided context. Ensure that your response is coherent, imaginative, and clearly relates to the given concept and context. Provide your response in plain text format as follows:

Metaphor/Analogy: [Your metaphor or analogy]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The metaphor or analogy should clearly relate to the given concept and context.",
            "The response should be creative and imaginative.",
            "The metaphor or analogy should be coherent and easy to understand.",
            "The response should not be a direct restatement of the concept or context, but rather a creative reimagining."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
