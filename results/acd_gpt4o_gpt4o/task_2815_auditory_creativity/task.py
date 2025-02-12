class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "soundscape", "description": "A serene forest with birds chirping, a gentle stream flowing, occasional rustling of leaves, and distant animal calls.", "instructions": "Write a short story inspired by the described soundscape. Your story should be between 300 and 500 words. Provide your story in plain text format."},
            "2": {"task": "music_piece", "description": "A classical piano piece with a melancholic yet hopeful melody, slow tempo, and dynamic variations.", "instructions": "Write a poem inspired by the described music piece. Your poem should be between 12 and 20 lines. Provide your poem in plain text format."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to generate creative content based on the following auditory description: {t['description']}. {t['instructions']}"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task"] == "soundscape":
            criteria = [
                "The story should be coherent and creatively inspired by the described soundscape.",
                "The story should be between 300 and 500 words.",
                "The response should be in plain text format."]
        elif t["task"] == "music_piece":
            criteria = [
                "The poem should be inspired by the described music piece and convey a matching mood.",
                "The poem should be between 12 and 20 lines.",
                "The response should be in plain text format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
