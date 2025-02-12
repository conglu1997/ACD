class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concept": "time",
                "example": "Generate a metaphor or an analogy for the concept of 'time' and explain its relevance."
            },
            "2": {
                "concept": "knowledge",
                "example": "Generate a metaphor or an analogy for the concept of 'knowledge' and explain its relevance."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a metaphor or an analogy for the following concept: '{t['concept']}'. After generating the metaphor or analogy, explain its relevance and how it helps to understand the concept better. Ensure that your response is original, creative, and clearly articulated. Your explanation should include the following elements:
1. A clear articulation of the metaphor or analogy.
2. How the metaphor or analogy relates to the concept.
3. Why this metaphor or analogy is insightful or helpful in understanding the concept.

Submit your response as a plain text string in the following format:

Metaphor/Analogy: [Your metaphor or analogy here]
Explanation: [Your explanation here]

For example:
Metaphor/Analogy: Time is like a river, flowing continuously and never stopping.
Explanation: The metaphor of time as a river helps to understand its continuous and unending nature. Just as a river flows without stopping, time moves forward relentlessly. This comparison highlights the unstoppable passage of time and the importance of making the most of each moment."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The metaphor or analogy should be original and directly relevant to the concept.",
            "The explanation should clearly outline the relevance and insightfulness of the metaphor or analogy.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
