class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"art_description": "A painting depicting a starry night with swirling clouds and a bright crescent moon. The village below is dark with sharp, geometric shapes, contrasting the fluidity of the sky."},
            "2": {"art_description": "A sculpture of a figure with elongated limbs and a serene expression, standing in a contemplative pose. The material is smooth and reflective, catching the light in interesting ways."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to provide an art critique and interpretation based on the given description of the artwork.

Art Description:
{t['art_description']}

Provide your critique in the form of a detailed analysis, discussing the following aspects:
1. The overall impression and emotional impact of the artwork.
2. The artistic style and techniques used.
3. The possible meaning or message conveyed by the artwork.
4. Any cultural or historical context that may be relevant.

Format your response as follows:

Art Critique:
1. [Overall impression and emotional impact]
2. [Artistic style and techniques]
3. [Possible meaning or message]
4. [Cultural or historical context]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The critique must address all specified aspects.",
            "The analysis should be coherent and insightful.",
            "The interpretation should be plausible and well-supported by the description."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
