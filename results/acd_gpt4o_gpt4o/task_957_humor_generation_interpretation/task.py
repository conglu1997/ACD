class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Why did the chicken cross the road?"},
            "2": {"joke": "I told my wife she was drawing her eyebrows too high. She looked surprised."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'prompt' in t:
            return f"""Your task is to generate a joke based on the given prompt:

Prompt: {t['prompt']}

Ensure that your response is humorous and follows the structure of a typical joke. The joke should be original and creative. Provide your response in plain text format. Here is an example format for your response:

Joke: [Your joke]

Example: Prompt: Why did the scarecrow win an award? Joke: Because he was outstanding in his field."""
        else:
            return f"""Your task is to interpret the humor in the given joke:

Joke: {t['joke']}

Provide a detailed explanation of why the joke is funny, including any linguistic nuances, cultural references, or wordplay involved. Your explanation should be thorough and insightful. Provide your response in plain text format. Here is an example format for your response:

Interpretation: [Your explanation]

Example: Joke: I told my wife she was drawing her eyebrows too high. She looked surprised. Interpretation: The humor in this joke comes from the play on words. The phrase 'looked surprised' is a pun because drawing eyebrows too high on the forehead can make someone appear surprised, and the wife's reaction of looking surprised adds to the humor."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'prompt' in t:
            criteria = ["The response should be a coherent joke.", "The joke should be based on the given prompt.", "The joke should be humorous.", "The joke should be original and creative."]
        else:
            criteria = ["The interpretation should accurately explain why the joke is funny.", "The explanation should include relevant linguistic nuances, cultural references, or wordplay.", "The explanation should be thorough and insightful."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
