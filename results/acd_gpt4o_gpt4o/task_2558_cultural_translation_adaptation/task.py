class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"original": "A Japanese folktale about a clever rabbit outsmarting a tiger. In the story, the rabbit uses its wit to trick the tiger into thinking there is a greater danger nearby, causing the tiger to flee and leave the rabbit unharmed.", "target_culture": "Western (American or European)"},
            "2": {"original": "An Indian story about a wise crow finding water in a desert. The crow sees a pot with a small amount of water at the bottom, and it cleverly drops pebbles into the pot until the water rises high enough for the crow to drink.", "target_culture": "Chinese"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        original = t["original"]
        target_culture = t["target_culture"]
        instructions = f"""Your task is to translate and adapt the following piece of content from its original cultural context to the target cultural context. Ensure that the adapted content remains culturally appropriate and retains the original meaning and essence of the story.

Original Content: {original}

Target Culture: {target_culture}

Provide your response in the following format:

Adapted Content: [Your adapted content]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The adapted content should be culturally appropriate within the target culture.",
            "The adapted content should retain the original meaning and essence of the story.",
            "The adaptation should demonstrate understanding of cultural nuances and context.",
            "The adapted content should be coherent and engaging." 
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
