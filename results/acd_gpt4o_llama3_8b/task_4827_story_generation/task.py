class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "A young girl discovers a hidden portal in her backyard that leads to a magical world."
            },
            "2": {
                "prompt": "An astronaut stranded on a distant planet must find a way to survive and communicate with Earth."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a story based on the following prompt:

Prompt: {t['prompt']}

Your story should be between 500 and 1000 words. Ensure that the narrative is coherent, engaging, and maintains context and character consistency throughout. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should be coherent and engaging.",
            "The narrative should maintain context and character consistency throughout.",
            "The story should be between 500 and 1000 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
