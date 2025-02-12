class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "technology",
                "joke": "Why don't scientists trust atoms? Because they make up everything!"
            },
            "2": {
                "theme": "sports",
                "joke": "Why did the scarecrow become a successful baseball player? Because he was outstanding in his field!"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a humorous joke based on the given theme and critique the provided joke.

Theme: {t['theme']}
Provided Joke: {t['joke']}

Your task is two-fold:
1. Generate an original joke based on the given theme. Ensure the joke is humorous, contextually appropriate, and not derived from well-known jokes.
2. Critique the provided joke, analyzing its humor, context, and any cultural references. Provide a detailed analysis of why the joke is or isn't funny.

Submit your response as a plain text string in the following format:

Generated Joke: [Your generated joke]
Critique: [Your critique of the provided joke]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The generated joke should be humorous and contextually appropriate.",
            "The critique should be detailed and analyze the humor, context, and cultural references of the provided joke."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
