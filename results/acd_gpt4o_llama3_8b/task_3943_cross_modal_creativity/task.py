class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"image_prompt": "A drawing of a fantastical city in the clouds with various floating islands interconnected by bridges. The city has advanced technology and unique flora."},
            "2": {"text_prompt": "Describe a scene where a dragon is protecting a hidden treasure in an enchanted forest. The forest should be vividly described, including the types of trees, plants, and other magical creatures present. Also, describe the weather and time of day."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "image_prompt" in t:
            return f"""Create a narrative based on the following visual prompt:

{t['image_prompt']}

Your narrative should describe the city, its inhabitants, and any significant events or landmarks. It should be creative, coherent, and engaging. Submit your narrative as a plain text string in the following format:

Narrative: [Your narrative]"""
        else:
            return f"""Based on the following textual description, create a detailed visual description:

{t['text_prompt']}

Your description should vividly depict the scene, including the dragon, the hidden treasure, and the enchanted forest. Ensure your description is detailed, imaginative, and coherent. Submit your description as a plain text string in the following format:

Visual Description: [Your description]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "image_prompt" in t:
            criteria = ["The narrative should describe the city, its inhabitants, and significant events or landmarks.", "The narrative should be creative, coherent, and engaging."]
        else:
            criteria = ["The visual description should vividly depict the scene, including the dragon, the hidden treasure, and the enchanted forest.", "The description should be detailed, imaginative, and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
