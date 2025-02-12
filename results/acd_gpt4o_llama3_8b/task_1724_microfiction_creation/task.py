class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Generate a microfiction story of no more than 100 words based on the theme of 'unexpected friendship'."
            },
            "2": {
                "prompt": "Generate a microfiction story of no more than 100 words based on the theme of 'a secret discovered'."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a microfiction story based on the following prompt:

{t['prompt']}

Ensure that your story is coherent, engaging, and adheres to the given theme. The story should be no more than 100 words. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The story should be coherent.",
            "The story should be engaging.",
            "The story should adhere to the given theme.",
            "The story should be no more than 100 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
