class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Why did the chicken cross the road?"
            },
            "2": {
                "joke": "Why don't scientists trust atoms? Because they make up everything!"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "prompt" in t:
            instructions = f"""Your task is to generate a joke based on the following prompt:

Prompt: {t['prompt']}

Provide your joke in the following format:

Joke:
[Your joke here]

Ensure that the joke is funny, appropriate, and follows a coherent structure."""
        else:
            instructions = f"""Your task is to critique the following joke based on its humor, appropriateness, and structure:

Joke: {t['joke']}

Provide your critique in the following format:

Critique:
[Your critique here]

Ensure that your critique is clear, logical, and covers all three aspects: humor, appropriateness, and structure."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "prompt" in t:
            criteria = [
                "The joke should be funny.",
                "The joke should be appropriate.",
                "The joke should follow a coherent structure."
            ]
        else:
            criteria = [
                "The critique should assess the humor of the joke.",
                "The critique should assess the appropriateness of the joke.",
                "The critique should assess the structure of the joke.",
                "The critique should be clear and logical."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
