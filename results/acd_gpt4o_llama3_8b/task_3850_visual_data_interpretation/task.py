class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "A photograph of a beach at sunset. The sky is filled with vibrant hues of orange and pink, with the sun partially visible on the horizon. There are a few people walking along the shoreline, and a couple of seagulls flying above the water. Nearby, a beach ball is lying on the sand, and a small bonfire is burning with two people sitting beside it."},
            "2": {"description": "A drawing of a bustling city street during the day. Tall buildings line both sides of the street, with cars and buses moving along the road. People are walking on the sidewalks, and there are street vendors selling various goods. In the background, a clock tower is visible, showing the time as noon. A child is holding a balloon, and a street musician is playing the guitar."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following description and provide a detailed account of the visual elements and context it represents. Then, generate a new description for a similar type of image.

Description: {t['description']}

Submit your response as a plain text string formatted as follows:

1. Interpretation: [Your detailed interpretation of the visual description]
2. New Description: [Your new description for a similar type of image]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The interpretation should accurately and comprehensively describe the visual elements and context of the given description.", "The new description should be coherent, detailed, and similar in type to the original image."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
