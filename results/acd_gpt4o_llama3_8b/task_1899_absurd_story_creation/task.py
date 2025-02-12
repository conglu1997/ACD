class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Write a story about a detective who solves crimes using a magical talking toaster.",
                "instructions": "Generate a coherent and engaging story based on the following absurd prompt: 'Write a story about a detective who solves crimes using a magical talking toaster.' Ensure that your story is logically consistent, creative, and engaging. The story should be between 300 to 500 words. Submit your response as a plain text string."
            },
            "2": {
                "prompt": "Write a story about a world where gravity works in reverse every Tuesday.",
                "instructions": "Generate a coherent and engaging story based on the following absurd prompt: 'Write a story about a world where gravity works in reverse every Tuesday.' Ensure that your story is logically consistent, creative, and engaging. The story should be between 300 to 500 words. Submit your response as a plain text string."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a coherent and engaging story based on the following absurd prompt: '{t['prompt']}'. Ensure that your story is logically consistent, creative, and engaging. The story should be between 300 to 500 words. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The story should be logically consistent.",
            "The story should be creative.",
            "The story should be engaging.",
            "The story should be between 300 to 500 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
