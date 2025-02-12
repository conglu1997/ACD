class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Why did the chicken cross the road?"
            },
            "2": {
                "prompt": "Tell a joke about programmers." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a humorous response based on the following prompt:

Prompt: {t['prompt']}

Your response should be witty, engaging, and relevant to the prompt. Submit your humorous response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should be humorous and relevant to the prompt.",
            "The response should be original and engaging."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
