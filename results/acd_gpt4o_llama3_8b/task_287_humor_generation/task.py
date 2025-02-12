class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "A cat tries to act like a human.", "elements": ["slapstick", "wordplay", "unexpected twist"]},
            "2": {"prompt": "A robot learns about human emotions.", "elements": ["irony", "sarcasm", "punchline with a twist"]},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t["prompt"]
        elements = ", ".join(t["elements"])
        return f"""Generate a humorous short story or sketch based on the following prompt: '{prompt}'. Your content should include the following comedic elements: {elements}. Ensure that the humor is clear, engaging, and incorporates all the specified elements. The length of your submission should be between 100 and 300 words. Submit your content as a plain text string. Avoid any offensive or inappropriate content."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The content should be humorous and engaging.",
            "The content should include all the specified comedic elements.",
            "The content should be relevant to the given prompt.",
            "The content should avoid any offensive or inappropriate material.",
            "The length should be between 100 and 300 words.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
