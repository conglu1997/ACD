class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Write a limerick about a clumsy cat.",
                "instructions": "Generate a humorous limerick about a clumsy cat. Ensure that the limerick follows the traditional AABBA rhyme scheme and is funny. Submit your response as a plain text string."
            },
            "2": {
                "prompt": "Write a couplet about a forgetful professor.",
                "instructions": "Generate a humorous couplet about a forgetful professor. Ensure that the couplet consists of two rhyming lines and is funny. Submit your response as a plain text string."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a humorous poem based on the following prompt: {t['prompt']} Ensure that the poem adheres to the specified poetic form and is funny. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The poem should adhere to the specified poetic form.",
            "The poem should be humorous.",
            "The language should be clear and creative."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
