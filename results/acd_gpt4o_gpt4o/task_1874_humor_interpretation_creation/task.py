class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"joke": "Why don't scientists trust atoms? Because they make up everything!", "theme": "science"},
            "2": {"joke": "I told my wife she was drawing her eyebrows too high. She looked surprised.", "theme": "everyday life"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves understanding and generating humor:

1. Interpret the following joke and provide a clear and concise explanation of its humor and context.

Joke: {t['joke']}

Please provide your interpretation in the following format:
- Explanation: [Your explanation]

2. Generate a new joke based on the given theme.

Theme: {t['theme']}

Ensure that your joke is original, funny, and contextually appropriate. Provide the generated joke in the following format:
- Joke: [Your joke]

Both parts of the task are equally important. Make sure your responses are clear and detailed."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        # Define criteria for evaluation
        criteria = [
            "The explanation should clearly convey the humor and context of the given joke.",
            "The generated joke should be original and funny.",
            "The generated joke should be contextually appropriate for the given theme."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
