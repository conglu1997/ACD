class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "technology",
                "example": "Generate a joke based on the theme 'technology' and explain why it is funny."
            },
            "2": {
                "theme": "animals",
                "example": "Generate a joke based on the theme 'animals' and explain why it is funny."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a joke based on the following theme: '{t['theme']}'. After generating the joke, explain why it is funny. Ensure that your joke is original, creative, and relevant to the theme. Your explanation should clearly outline the elements of humor used in the joke and why it is expected to be funny to an audience. Submit your response as a plain text string in the following format:

Joke: [Your joke here]
Explanation: [Your explanation here]

For example:
Joke: Why don't programmers like nature? Because it has too many bugs.
Explanation: The joke is funny because it plays on the double meaning of the word 'bugs.' In nature, bugs are insects, but in programming, 'bugs' refer to errors in the code. The humor arises from the clever wordplay and the relatable frustration programmers feel towards bugs in their code."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The joke should be original and relevant to the theme.",
            "The explanation should clearly outline the elements of humor and why the joke is funny.",
            "The joke and explanation should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
