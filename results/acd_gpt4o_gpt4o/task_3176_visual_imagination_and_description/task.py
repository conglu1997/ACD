class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "A bustling medieval marketplace at sunset"},
            "2": {"description": "The sun is setting, casting a golden hue over the bustling marketplace. Stalls lined with colorful fabrics and exotic spices create a vibrant tapestry. Merchants shout their wares as children weave through the crowd. A musician plays a lively tune on a wooden flute, while a blacksmith hammers away at his forge. In the distance, the silhouette of a grand castle looms."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "prompt" in t:
            instructions = f"""Your task is to generate a detailed visual description based on the following prompt: {t['prompt']}.

Ensure your description is vivid, detailed, and captures the essence of the scene. Provide your description in plain text format, structured as follows:

Description: [Your detailed description]
"""
        else:
            instructions = f"""Your task is to interpret the following detailed visual description and create a coherent narrative based on it:

{t['description']}

Ensure your narrative is engaging, logically structured, and captures the essence of the described scene. Provide your narrative in plain text format, structured as follows:

Narrative: [Your narrative]
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "prompt" in t:
            criteria = [
                "The description should be vivid and detailed.",
                "The description should capture the essence of the scene described in the prompt."
            ]
        else:
            criteria = [
                "The narrative should be coherent and logically structured.",
                "The narrative should capture the essence of the described scene.",
                "The narrative should be engaging and reflect the details given in the description."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
