class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a flash fiction story about an unexpected encounter in an abandoned building.", "word_limit": 150},
            "2": {"prompt": "Write a flash fiction story about a mysterious letter that changes someone's life.", "word_limit": 150}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t["prompt"]
        word_limit = t["word_limit"]
        instructions = f"""Your task is to write a complete flash fiction story based on the following prompt, adhering to a strict word limit:

Prompt: {prompt}

Word Limit: {word_limit} words

Ensure that your story is coherent, creative, and compelling. Provide your story in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should be coherent and logically structured.",
            "The story should be creative and engaging.",
            "The story should adhere to the given word limit."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
