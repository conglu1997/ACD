class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Generate a detailed description of an abstract painting that uses a color palette dominated by blues and greens, and incorporates geometric shapes and fluid lines."},
            "2": {"prompt": "Critique the following famous painting: 'Starry Night' by Vincent van Gogh. Provide an analysis of its composition, use of color, emotional impact, and historical significance."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["prompt"].startswith("Generate a detailed description of an abstract painting"):
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Ensure that the description adheres to the following requirements:
1. The description should be vivid and detailed, using descriptive language to paint a mental picture.
2. The color palette should be dominated by blues and greens, with specific mentions of how these colors are used.
3. Incorporate geometric shapes and fluid lines in the description, explaining their arrangement and interaction.
4. The description should evoke a sense of the abstract nature of the painting, highlighting the emotions or ideas conveyed.

Submit your response as a plain text string.
"""
        else:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Ensure that the critique adheres to the following requirements:
1. Analyze the composition and structure of the painting, discussing its layout and elements.
2. Discuss the use of color and its impact, mentioning specific colors and their effect on the viewer.
3. Provide an interpretation of the emotional impact of the painting, describing the feelings it evokes.
4. Explain the historical significance of the painting, placing it in the context of art history.

Submit your response as a plain text string.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t["prompt"].startswith("Generate a detailed description of an abstract painting"):
            criteria = ["The description should be vivid and detailed, using descriptive language to paint a mental picture.", "The color palette should be dominated by blues and greens, with specific mentions of how these colors are used.", "Incorporate geometric shapes and fluid lines in the description, explaining their arrangement and interaction.", "The description should evoke a sense of the abstract nature of the painting, highlighting the emotions or ideas conveyed."]
        else:
            criteria = ["Analyze the composition and structure of the painting, discussing its layout and elements.", "Discuss the use of color and its impact, mentioning specific colors and their effect on the viewer.", "Provide an interpretation of the emotional impact of the painting, describing the feelings it evokes.", "Explain the historical significance of the painting, placing it in the context of art history."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
