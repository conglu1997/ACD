class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "A painting featuring abstract geometric shapes in vibrant colors, with no clear representational forms. The background is a gradient of blues and purples, and the shapes seem to be floating in an undefined space."},
            "2": {"description": "A sculpture made from recycled materials, depicting a human figure in a distorted, fragmented form. The figure's limbs are disproportionately long, and the head is composed of various mechanical parts."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret and critique the following modern art piece based on the given description:

{t['description']}

Your critique should include:
1. An interpretation of the possible meaning or message behind the art piece.
2. An analysis of the techniques and materials used by the artist.
3. Your personal critique, including both strengths and weaknesses of the piece.

Ensure your response is insightful, well-structured, and articulates a clear understanding of modern art concepts. Submit your critique as a plain text string in the following format:

Critique: [Your Critique Here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The critique should include an interpretation of the meaning, an analysis of techniques and materials, and a personal critique with strengths and weaknesses.", "The critique should be insightful, well-structured, and articulate a clear understanding of modern art concepts."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
