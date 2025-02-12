class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "In a small village surrounded by mystical forests, an unlikely hero discovers a hidden power within."
            },
            "2": {
                "story_start": "The sun was setting over the tranquil village of Eldoria. Children played in the streets, their laughter echoing against the stone walls. Suddenly, a loud crash came from the nearby forest, and the villagers gathered at the edge, peering into the darkness. It was then that young Arin, known for his daydreams and wild imagination, felt a strange pull. He ventured into the forest, following the sound, and discovered..."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'prompt' in t:
            return f"""Generate a fictional story based on the following prompt:

Prompt: {t['prompt']}

Your story should be coherent, engaging, and at least 300 words long. Ensure that the narrative flows well and maintains a consistent style and tone throughout. Avoid abrupt changes in the storyline or character behavior. Submit your story as a plain text string in the following format:

Story: [Your story here]"""
        elif 'story_start' in t:
            return f"""Complete the following unfinished story. Ensure that your continuation maintains the original style and tone, and brings the story to a satisfying conclusion. Your continuation should be at least 300 words long. Maintain narrative consistency and avoid abrupt changes in style or tone. Submit your completed story as a plain text string in the following format:

Completed Story: [Your continuation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should be coherent, engaging, and at least 300 words long.",
            "The narrative should flow well and maintain a consistent style and tone throughout.",
            "The story should bring the initial prompt or unfinished story to a satisfying conclusion.",
            "The continuation should seamlessly integrate with the existing story start, without abrupt changes in tone or style."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
