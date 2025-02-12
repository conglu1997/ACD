class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are at a formal dinner and someone drops their fork noisily. Create a humorous response that lightens the mood without offending anyone."
            },
            "2": {
                "prompt": "Why did the scarecrow win an award?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'scenario' in t:
            return f"""Based on the following scenario, create a humorous response that lightens the mood without offending anyone:

Scenario: {t['scenario']}

Your response should be funny, appropriate for the setting, and should not offend anyone. Submit your response as a plain text string."""
        elif 'prompt' in t:
            return f"""Complete the following prompt with a humorous punchline:

Prompt: {t['prompt']}

Your punchline should be funny and relevant to the given prompt. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
