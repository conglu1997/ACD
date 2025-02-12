class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "office humor",
                "constraints": ["Include a pun", "Must be suitable for a professional setting"]
            },
            "2": {
                "theme": "technology humor",
                "constraints": ["Include a play on words", "Must reference a well-known tech company"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a piece of humorous content based on the following theme and constraints:

Theme: {t['theme']}
Constraints:
{chr(10).join('- ' + constraint for constraint in t['constraints'])}

Your content should be a short joke, anecdote, or humorous statement that aligns with the given theme and constraints. Ensure that the humor is appropriate for the specified context.

Submit your response in the following format:

Humorous Content: [Your humorous content here]

Example response format:
Humorous Content: Why don't programmers like nature? It has too many bugs.

For Task 1: Why did the scarecrow become a successful manager? Because he was outstanding in his field.

For Task 2: I would tell you a joke about UDP, but I'm not sure if you'd get it."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The content should be humorous and align with the given theme.",
            "The content should meet the specified constraints.",
            "The humor should be appropriate for the specified context.",
            "For Task 1: The content must include a pun suitable for a professional setting.",
            "For Task 2: The content must include a play on words and reference a well-known tech company."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
