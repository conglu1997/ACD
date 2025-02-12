class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Imagine you are standing on a beach at sunset. Describe the sensory experience in terms of sight, sound, smell, touch, and taste."},
            "2": {"description": "The aroma of freshly baked bread wafted through the air, mingling with the faint scent of lavender from a nearby field. The gentle hum of bees buzzing and the distant murmur of a brook provided a soothing soundtrack. The sunlight filtered through the trees, casting dappled shadows on the ground, while a cool breeze brushed against the skin. The taste of the bread, warm and slightly sweet, melted in the mouth, bringing a comforting sense of home."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "prompt" in t:
            instructions = f"""Your task is to generate a rich, vivid sensory description based on the following prompt:

{t['prompt']}

Ensure that your description is detailed and covers all five senses (sight, sound, smell, touch, and taste). Be as descriptive and evocative as possible. Provide your response in plain text format."""
        else:
            instructions = f"""Your task is to interpret the following sensory description and identify the specific sensory details mentioned for each of the five senses (sight, sound, smell, touch, and taste). Provide your interpretation in a clear and organized format.

Description: {t['description']}"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "prompt" in t:
            criteria = [
                "The response should include detailed and vivid descriptions for all five senses.",
                "The descriptions should be evocative and paint a clear sensory picture."]
        else:
            criteria = [
                "The interpretation should accurately identify the sensory details for each of the five senses.",
                "The interpretation should be clear and organized."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
