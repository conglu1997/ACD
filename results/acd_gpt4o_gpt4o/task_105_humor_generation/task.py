class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'prompt': 'Why did the scarecrow win an award?'},
            '2': {'prompt': 'Write a humorous short story about a day in the life of a talking refrigerator.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate humor based on the given prompt. Make sure your response is funny, clever, and appropriate for a general audience. Keep your response concise and directly related to the prompt.

Prompt: {t['prompt']}

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should be humorous.", "The humor should be appropriate for a general audience.", "The response should directly relate to the given prompt."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
