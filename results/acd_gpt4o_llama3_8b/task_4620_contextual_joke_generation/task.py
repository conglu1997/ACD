class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "context": "At a doctor's office",
                "description": "Generate a joke that would be appropriate and humorous in a doctor's office setting."
            },
            "2": {
                "context": "During a job interview",
                "description": "Generate a joke that would be appropriate and humorous during a job interview."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a joke based on the following context. Ensure that the joke is appropriate for the given scenario and is humorous. Provide a brief explanation of why the joke fits the context and why it is funny. Submit your response as a plain text string in the following format:

Context: {t['context']}

- Joke: [Your joke]
- Explanation: [Your explanation]

Hint: The joke should be original, culturally sensitive, and suitable for the given setting. Avoid using common or overused jokes."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The joke should be appropriate for the given context.",
            "The joke should be original and humorous.",
            "The explanation should clearly state why the joke fits the context and why it is funny."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
