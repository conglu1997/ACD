class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "type": "joke_generation",
                "prompt": "Why did the computer go to the doctor?"
            },
            "2": {
                "type": "joke_analysis",
                "joke": "Parallel lines have so much in common. It’s a shame they’ll never meet."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "joke_generation":
            prompt = t["prompt"]
            instructions = f"""Your task is to generate a humorous response to the given prompt.

Prompt: {prompt}

Your joke should be:
1. Creative and original.
2. Understandable and clear.
3. Contextually appropriate.
4. Include a punchline.

Provide your joke in plain text format.
"""
        elif t["type"] == "joke_analysis":
            joke = t["joke"]
            instructions = f"""Your task is to analyze the given joke and explain why it is humorous.

Joke: {joke}

Your analysis should cover:
1. The linguistic elements that make the joke funny.
2. The cultural or contextual aspects that contribute to the humor.
3. Any wordplay or puns used in the joke.
4. The underlying logic or reasoning that adds to the humor.
5. Ensure clarity and depth in your analysis.

Provide your analysis in plain text format.
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "joke_generation":
            criteria = [
                "The joke should be creative and original.",
                "The joke should be understandable and clear.",
                "The joke should be contextually appropriate.",
                "The joke should include a punchline."
            ]
        elif t["type"] == "joke_analysis":
            criteria = [
                "The analysis should accurately identify the linguistic elements that make the joke funny.",
                "The analysis should cover cultural or contextual aspects that contribute to the humor.",
                "The analysis should identify any wordplay or puns used in the joke.",
                "The analysis should explain the underlying logic or reasoning that adds to the humor.",
                "The analysis should ensure clarity and depth."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
