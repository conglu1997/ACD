class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"art_description": "A painting depicting a serene landscape with rolling hills, a calm river, and a vibrant sunset in the background. The colors are warm and inviting, with the sun casting a golden hue over the scene."},
            "2": {"art_description": "A modern abstract sculpture made of metal and glass, featuring sharp angles and reflective surfaces. The piece is designed to evoke a sense of chaos and complexity, with different shapes intersecting in unexpected ways."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to evaluate and critique the following piece of visual art based on the provided description:

Description: {t['art_description']}

Your critique should include the following elements:
1. An overall impression of the piece.
2. An analysis of the use of color, form, and composition.
3. A discussion of the emotional and conceptual impact of the art.
4. Any cultural or historical references that may be relevant.

Your critique should be clear, well-structured, and detailed. Provide your response in the following format:

Overall Impression: <your overall impression>
Analysis: <your analysis>
Impact: <your discussion of the emotional and conceptual impact>
References: <any cultural or historical references>"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        # Define criteria for evaluation
        criteria = [
            "The critique should include an overall impression of the piece.",
            "The critique should analyze the use of color, form, and composition.",
            "The critique should discuss the emotional and conceptual impact of the art.",
            "The critique should mention any relevant cultural or historical references.",
            "The critique should be coherent and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
