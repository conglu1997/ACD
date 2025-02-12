class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "joke_generation", "prompt": "Why did the scarecrow win an award?"},
            "2": {"task_type": "funny_story_generation", "prompt": "Write a funny story about a day in the life of a talking dog."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'joke_generation':
            return f"Generate a punchline for the following joke prompt: {t['prompt']}. Ensure the punchline is a single sentence, humorous, and original. Format your response as: Punchline: [Your punchline].\nExample: Punchline: Because he was outstanding in his field."
        elif t['task_type'] == 'funny_story_generation':
            return f"Generate a funny story based on the following prompt: {t['prompt']}. Ensure the story is at least 150 words long, humorous, and original. Format your response as: Story: [Your funny story].\nExample: Story: One day, the talking dog decided to run for mayor. His campaign slogan was 'A bone in every yard!'..."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should be humorous and appropriate.",
            "The humor should be contextually relevant to the prompt.",
            "The joke punchline should be a single sentence.",
            "The funny story should be at least 150 words long.",
            "The humor should be original and not copied from known jokes or stories."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
