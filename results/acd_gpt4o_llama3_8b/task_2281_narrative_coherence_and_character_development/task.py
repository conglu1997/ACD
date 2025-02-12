class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Write the first segment of a story that introduces the main character and sets up a conflict. The main character is a detective in a futuristic city dealing with a mysterious disappearance. The segment should be between 150 and 300 words. Submit your segment as a plain text string."
            },
            "2": {
                "prompt": "Continue the story from the first segment. Develop the character of the detective further and introduce a secondary character who helps in the investigation. Ensure the segment includes a surprising plot twist. The segment should be between 150 and 300 words. Submit your segment as a plain text string."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return t['prompt']

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The narrative should be coherent and engaging.",
            "The character development should be consistent and believable.",
            "The segment should be between 150 and 300 words.",
            "The second segment should include a surprising plot twist."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
