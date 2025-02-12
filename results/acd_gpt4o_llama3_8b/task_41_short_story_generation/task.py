class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "characters": "A young wizard named Arin, and a talking cat named Whiskers.",
                "setting": "A magical forest with glowing plants, hidden dangers, and a mysterious ancient tree at its heart.",
                "theme": "Friendship, bravery, and the discovery of one's true potential."
            },
            "2": {
                "characters": "A retired detective named Sam, and a mysterious stranger who knows a secret about Sam's past.",
                "setting": "A small coastal town during a storm, with power outages, crashing waves, and an old lighthouse that holds a crucial clue.",
                "theme": "Mystery, redemption, and the uncovering of buried truths."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a fictional short story based on the following constraints:

Characters: {t['characters']}
Setting: {t['setting']}
Theme: {t['theme']}

Ensure your story is at least 500 words long and captures the essence of the given characters, setting, and theme. The story should be coherent, engaging, and follow a clear narrative structure. Submit your story as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The story should be at least 500 words long.",
            "The story should capture the essence of the given characters, setting, and theme.",
            "The story should be coherent, engaging, and follow a clear narrative structure."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
