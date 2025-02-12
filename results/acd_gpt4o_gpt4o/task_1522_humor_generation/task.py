class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Write a funny response to the following scenario: You accidentally sent a romantic text to your boss instead of your partner.",
                "style": "sarcastic"
            },
            "2": {
                "prompt": "Describe a humorous situation that could happen during a virtual work meeting.",
                "style": "light-hearted"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a humorous response based on the following prompt and style:\n\nPrompt: {t['prompt']}\n\nStyle: {t['style']}\n\nEnsure your response adheres to the given style and is both creative and funny. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should adhere to the given style (e.g., sarcastic, light-hearted).",
            "The response should be creative and humorous.",
            "The response should be relevant to the given prompt."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
