class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"cultural_reference": "Shakespearean plays", "prompt": "Create a humorous dialogue between two characters from a Shakespearean play. Ensure the humor is appropriate for the context and characters. The dialogue should be between 150 and 300 words."},
            "2": {"cultural_reference": "Greek mythology", "prompt": "Write a funny short story involving characters from Greek mythology. The humor should be rooted in the personalities and stories of the mythological characters. The short story should be between 200 and 400 words."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate humorous content based on the given cultural reference.

Cultural reference: {t['cultural_reference']}
Prompt: {t['prompt']}

Ensure that your response is witty, culturally appropriate, and captures the essence of the reference. Additionally, ensure historical and cultural accuracy in your response. Provide your response in plain text format and adhere to the specified word count range."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should be witty and humorous.",
            "The humor should be culturally appropriate and aligned with the given reference.",
            "The response should capture the essence of the cultural reference.",
            "The response should adhere to the specified word count range.",
            "The response should maintain historical and cultural accuracy."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
