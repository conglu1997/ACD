class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a short story about a lost puppy who finds its way home."},
            "2": {"prompt": "Write a short story about an unexpected friendship between a robot and a human."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write a short creative story based on the following prompt: '{t["prompt"]}'. The story should be coherent, engaging, and have a clear beginning, middle, and end. The response should be in prose format and should not exceed 300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should be coherent.",
            "The story should be engaging.",
            "The story should have a clear beginning, middle, and end.",
            "The story should not exceed 300 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
