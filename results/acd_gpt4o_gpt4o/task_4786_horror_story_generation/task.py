class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a short horror story set in an abandoned hospital. The story should build suspense and have a surprising twist at the end."},
            "2": {"prompt": "Analyze the following short horror story and provide feedback on its narrative structure, suspense building, and twist ending. Suggest improvements where necessary.", "story": "The old mansion had stood abandoned for decades, a silent sentinel in the midst of the forest. One night, a group of friends dared to enter, only to find themselves trapped in a nightmarish loop, where every exit led them back to the same room. As fear turned to panic, they discovered a chilling truth: they were not alone. The spirits of those who had perished in the mansion's dark past were with them, replaying their final moments over and over."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'prompt' in t and 'story' not in t:
            return f"""Your task is to generate a short horror story based on the following prompt.

Prompt:
{t['prompt']}

Instructions:
1. Write a short horror story (approximately 500 words) that adheres to the prompt.
2. Ensure the story builds suspense and includes a surprising twist at the end.

Your response should be in the following format:
Story: [Your horror story]"""
        elif 'story' in t:
            return f"""Your task is to analyze the following short horror story and provide feedback.

Story:
{t['story']}

Instructions:
1. Analyze the narrative structure, suspense building, and twist ending of the story.
2. Provide feedback and suggest improvements where necessary.

Your response should be in the following format:
Analysis: [Your analysis]
Feedback: [Your feedback and suggestions]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'prompt' in t:
            criteria = ["The story should adhere to the prompt.", "The story should build suspense effectively.", "The story should have a surprising twist at the end."]
        elif 'story' in t:
            criteria = ["The analysis should cover narrative structure, suspense building, and twist ending.", "The feedback should be constructive and suggest improvements."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
