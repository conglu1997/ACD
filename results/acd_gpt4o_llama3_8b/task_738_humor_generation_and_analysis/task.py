class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "A talking dog walks into a bar and..."
            },
            "2": {
                "joke": "Why don't scientists trust atoms? Because they make up everything!"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'prompt' in t:
            return f"""Generate a humorous story based on the following prompt. Ensure the story is creative, coherent, and genuinely funny. The story should be at least 100 words long. Submit your story as a plain text string.\n\nPrompt: {t['prompt']}"""
        elif 'joke' in t:
            return f"""Analyze the humor in the following joke. Explain why it is funny, considering linguistic nuances, cultural references, and timing. Provide your analysis in the following format:\n\n1. Explanation of the joke's structure.\n2. Linguistic nuances involved.\n3. Cultural references or context.\n4. Why it is funny.\n\nSubmit your analysis as a plain text string.\n\nJoke: {t['joke']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'prompt' in t:
            validation_criteria = [
                "The story should be creative, coherent, and genuinely funny.",
                "The story should be at least 100 words long."
            ]
        else:
            validation_criteria = [
                "The analysis should accurately explain why the joke is funny, considering linguistic nuances, cultural references, and timing.",
                "The analysis should follow the provided format."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
