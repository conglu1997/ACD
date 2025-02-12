class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "A cat wearing sunglasses, sitting on a beach chair with a drink in its paw."},
            "2": {"description": "A dog in a superhero costume, flying through the sky with a cape billowing behind."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t['description']
        return f"""You are given a visual description of a scene. Your task is to generate a humorous caption or dialogue that fits the described scene. Ensure that your response is witty, funny, and relevant to the visual elements described.

Visual Description: {description}

Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should be humorous.",
            "The response should be relevant to the visual description."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
