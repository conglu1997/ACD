class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"artwork_description": "A painting of a serene landscape featuring a river, mountains, and a sunset. The colors are vibrant and warm, creating a peaceful ambiance. The composition includes a large tree on the left side, and the river meanders through the center, reflecting the colors of the sunset."},
            "2": {"creation_criteria": "Create a detailed description of a surrealistic painting that includes a floating castle, a giant clock, and a whimsical forest. The painting should evoke a sense of mystery and wonder, with a dreamlike quality."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'artwork_description' in t:
            return f"""Your task is to critique the following piece of artwork based on its description.

Artwork Description:
{t['artwork_description']}

Instructions:
1. Provide a detailed critique of the artwork, discussing its composition, use of color, and emotional impact.
2. Suggest potential improvements or changes to enhance the artwork.

Your response should be in the following format:
Critique: [Your critique]
Suggestions: [Your suggestions]"""
        elif 'creation_criteria' in t:
            return f"""Your task is to create a detailed description of a new piece of artwork based on the given criteria.

Creation Criteria:
{t['creation_criteria']}

Instructions:
1. Provide a detailed description of the new artwork, ensuring that it includes all the specified elements.
2. Ensure that your description is vivid and coherent, capturing the essence of the surrealistic style.

Your response should be in the following format:
Description: [Your description]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'artwork_description' in t:
            criteria = ["The critique should discuss the composition, use of color, and emotional impact of the artwork.", "The suggestions should be relevant and aimed at enhancing the artwork."]
        elif 'creation_criteria' in t:
            criteria = ["The description should include all specified elements in a coherent and vivid manner.", "The description should capture the essence of the surrealistic style."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
