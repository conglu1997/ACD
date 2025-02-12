class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a short story about a lost puppy who finds its way home."},
            "2": {"prompt": "Write a short story about an unexpected friendship between a robot and a human."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to write a short creative story based on the following prompt: '{t["prompt"]}'. The story should be between 200 and 400 words long. Make sure it has a clear beginning, middle, and end."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should be between 200 and 400 words long.",
            "The story should have a clear beginning, middle, and end.",
            "The story should be coherent and contextually appropriate.",
            "The story should be creative and engaging."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
