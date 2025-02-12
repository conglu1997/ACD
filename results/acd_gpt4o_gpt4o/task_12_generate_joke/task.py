class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Why did the chicken cross the road?"},
            "2": {"prompt": "How many programmers does it take to change a light bulb?"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a joke based on the following prompt:

Prompt: {t["prompt"]}

The joke should be funny, coherent, and make sense in the context of the prompt. It should be a single sentence and provide a humorous punchline. Provide your joke in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The joke should be funny.", "The joke should be coherent.", "The joke should make sense in the context of the prompt.", "The joke should be a single sentence.", "The joke should provide a humorous punchline."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
