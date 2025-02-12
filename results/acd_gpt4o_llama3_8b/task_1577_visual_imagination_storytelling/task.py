class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "A dense, enchanted forest with trees that touch the sky, glowing flowers, and mystical creatures hiding behind the foliage."
            },
            "2": {
                "description": "An ancient, abandoned city submerged underwater, with sea creatures swimming through the ruins and corals growing on the old buildings."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate an imaginative and detailed story based on the following visual prompt:

Visual Description: {t['description']}

Your story should be between 300 to 500 words and should vividly describe the scene, incorporating elements from the visual description. The story should be coherent, engaging, and should paint a clear picture of the scene in the reader's mind. Focus on making the story immersive and captivating.

Submit your story as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The story should be between 300 to 500 words.", "The story should vividly describe the scene, incorporating elements from the visual description.", "The story should be coherent, engaging, and immersive."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
