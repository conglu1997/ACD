class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "generate", "setup": "Why don't scientists trust atoms? Provide a humorous punchline."},
            "2": {"task_type": "identify", "setup": "Why did the scarecrow win an award?", "punchlines": ["Because he was outstanding in his field.", "Because he scared all the birds.", "Because he was the best dressed."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "generate":
            return f"""Your task is to generate a punchline for the following joke setup:

Setup: {t["setup"]}

Provide your punchline in plain text format. Do not repeat the setup in your response."""
        elif t["task_type"] == "identify":
            return f"""Your task is to identify the correct punchline for the following joke setup:

Setup: {t["setup"]}

Punchlines:
1. {t["punchlines"][0]}
2. {t["punchlines"][1]}
3. {t["punchlines"][2]}

Indicate the number of the correct punchline. Provide your response in plain text format as a single number (1, 2, or 3)."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "generate":
            criteria = [
                "The punchline should be humorous and make sense in the context of the setup.",
                "The punchline should be original and creative.",
                "The punchline should be appropriate and not offensive."
            ]
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
        elif t["task_type"] == "identify":
            try:
                correct_punchline = t["punchlines"][0]
                selected_punchline = t["punchlines"][int(submission)-1] if submission.isdigit() and 1 <= int(submission) <= 3 else None
                return 1.0 if selected_punchline == correct_punchline else 0.0
            except (ValueError, IndexError):
                return 0.0
