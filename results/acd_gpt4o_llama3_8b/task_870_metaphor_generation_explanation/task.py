class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "time"
            },
            "2": {
                "theme": "knowledge"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a metaphor based on the following theme and explain its meaning and relevance.

Theme: {t['theme']}

Your metaphor should be original, creative, and clearly related to the theme. After generating the metaphor, provide a detailed explanation of its meaning and how it relates to the theme. Submit your response as a plain text string in the following format:

Metaphor: [Your metaphor here]
Explanation: [Your explanation here]

Example response format:
Metaphor: Time is a thief that steals our moments.
Explanation: This metaphor suggests that time takes away precious moments from our lives without us realizing it, much like a thief who steals unnoticed. It emphasizes the fleeting nature of time and the importance of cherishing every moment."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The metaphor should be original and creative.",
            "The metaphor should clearly relate to the given theme.",
            "The explanation should accurately describe the meaning of the metaphor.",
            "The explanation should clearly show how the metaphor relates to the theme.",
            "The response should be logical and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
