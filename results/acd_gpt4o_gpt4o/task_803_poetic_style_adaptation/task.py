class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a poem about the beauty of nature in the style of William Wordsworth."},
            "2": {"prompt": "Compose a poem about the melancholic passage of time in the style of Edgar Allan Poe."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to generate a poem based on the given prompt. Here is the prompt:\n{t['prompt']}\nPlease ensure that your poem reflects the style and thematic elements typical of the specified poet. Provide your submission in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The poem should reflect the style and thematic elements typical of the specified poet."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
