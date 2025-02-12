class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Express the feeling of excitement about a new job using only emojis. Ensure the sequence is between 3 to 6 emojis."},
            "2": {"prompt": "Interpret the following emoji sequence and describe the scenario it represents: 🌧️➡️🏠➡️☕➡️📖. Provide a detailed description of the scenario in plain text."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to perform the following emoji-related task:

Prompt: {t['prompt']}

For Task 1: Generate an emoji sequence that conveys the specified emotion or scenario. Ensure the sequence is between 3 to 6 emojis. Provide your response in the form of emojis only.
For Task 2: Interpret the given emoji sequence and describe in plain text the scenario it represents. Ensure your response is coherent and accurately captures the intended meaning of the emojis.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should accurately convey the specified emotion or scenario using emojis.", "The interpretation should be logical and coherent.", "The response should be creative and contextually appropriate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
