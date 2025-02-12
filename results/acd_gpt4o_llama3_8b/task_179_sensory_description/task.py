class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Describe the experience of walking through a dense forest on a foggy morning. Include details about the sights, sounds, smells, and textures you might encounter."},
            "2": {"prompt": "Describe the sensation of holding a warm cup of coffee on a chilly day. Include details about the warmth, aroma, and the feeling of the cup in your hands."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t["prompt"]
        return f"""Generate a detailed description of the following sensory experience:

{prompt}

Ensure your description is vivid, engaging, and captures the essence of the sensory experience. Use descriptive language to convey the sights, sounds, smells, textures, and any other relevant sensory details. Submit your description as a plain text string in the following format:

Description: [Your detailed description here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should be vivid and engaging.",
            "The description should capture the essence of the sensory experience.",
            "The description should use descriptive language to convey sensory details."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
