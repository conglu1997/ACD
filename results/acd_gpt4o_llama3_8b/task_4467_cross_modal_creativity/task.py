class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_type": "text_to_art",
                "text_description": "A serene landscape with a river winding through a dense forest, a small wooden cabin on the riverbank, and mountains in the background with a setting sun casting a golden hue."
            },
            "2": {
                "task_type": "art_to_text",
                "image_description": "A black-and-white sketch of a bustling medieval marketplace, with vendors selling various goods, people in period clothing, and a castle visible in the background."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "text_to_art":
            return f"""Create a detailed visual representation based on the following textual description: \n\n{t['text_description']}\n\nSubmit your response as a plain text string describing your visual representation in detail, including specific elements and their placement."""
        elif t["task_type"] == "art_to_text":
            return f"""Create a detailed textual description based on the following image description: \n\n{t['image_description']}\n\nSubmit your response as a plain text string. Ensure your description includes specific details about the scene, characters, and objects present."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "text_to_art":
            criteria = ["The visual representation should accurately reflect the given textual description, including specific elements and their placement."]
        elif t["task_type"] == "art_to_text":
            criteria = ["The textual description should accurately reflect the given image description, including specific details about the scene, characters, and objects present."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
