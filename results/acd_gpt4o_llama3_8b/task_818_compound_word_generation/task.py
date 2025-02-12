class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "components": ["sun", "flower"],
                "context": "a common garden plant"
            },
            "2": {
                "components": ["moon", "light"],
                "context": "a natural phenomenon visible at night"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a compound word or phrase using the given components and explain its meaning based on the context provided.

Components: {', '.join(t['components'])}
Context: {t['context']}

Your response should include:
1. The compound word or phrase.
2. A brief explanation of its meaning and usage in the given context.

Ensure your explanation is clear, logically structured, and demonstrates an understanding of the semantic relationship between the components. Submit your response as a plain text string in the following format:
- Compound Word or Phrase: [Your compound word or phrase]
- Explanation: [Your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should include a compound word or phrase.",
            "The explanation should logically follow from the given components and context.",
            "The response should demonstrate an understanding of the semantic relationship between the components.",
            "The explanation should be clear and logically structured.",
            "The response should follow the specified format precisely."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
