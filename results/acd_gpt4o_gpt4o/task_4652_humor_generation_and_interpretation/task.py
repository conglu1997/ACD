class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"joke": "Why don't scientists trust atoms? Because they make up everything!", "instruction": "Interpret the given joke and explain why it is humorous."},
            "2": {"theme": "office life", "instruction": "Generate a humorous anecdote related to office life. Ensure that your anecdote is creative, funny, and coherent. The anecdote should be at least 150 words long."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'joke' in t:
            instructions = f"""Your task is to interpret the following joke and explain why it is humorous:

Joke: {t['joke']}

Provide your explanation in plain text format. Ensure that your response captures the essence of the humor, including any wordplay, cultural references, or contextual elements that contribute to the joke's humor."""
        else:
            instructions = f"""Your task is to generate a humorous anecdote related to the following theme:

Theme: {t['theme']}

Ensure that your anecdote is creative, funny, and coherent. The anecdote should be at least 150 words long. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'joke' in t:
            criteria = [
                "The explanation should capture the essence of the humor.",
                "The explanation should include any wordplay, cultural references, or contextual elements that contribute to the joke's humor."]
        else:
            criteria = ["The anecdote should be creative, funny, and coherent.", "The anecdote should be at least 150 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
