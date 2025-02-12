class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Write a short story about a young boy who discovers a hidden door in his attic.",
                "length": "500-700 words"
            },
            "2": {
                "initial_text": "Sarah had always wondered about the old diary she found in her grandmother's attic. One day, she decided to open it and...",
                "length": "300-500 words"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "prompt" in t:
            return f"Your task is to generate a short story based on the following prompt:\n\nPrompt: {t['prompt']}\n\nYour story should be between {t['length']} words. Ensure that your story is coherent, engaging, and follows a logical narrative structure. Include the word count at the end of your story."
        else:
            return f"Your task is to continue the following story:\n\nInitial Text: {t['initial_text']}\n\nYour continuation should be between {t['length']} words. Ensure that your continuation is coherent, engaging, and follows a logical narrative structure. Include the word count at the end of your continuation."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should be coherent and logically structured.",
            "The story should be engaging and creative.",
            "The length should be within the specified word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
