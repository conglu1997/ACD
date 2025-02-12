class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "loneliness"
            },
            "2": {
                "poem": "The stars above are shining bright,\nIn the quiet of the night.\nBut in my heart, a silent cry,\nFor someone lost, a last goodbye."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "theme" in t:
            instructions = f"""Your task is to generate a poem based on the following theme: '{t['theme']}'.\n\nYour poem should be at least 8 lines long, maintain a consistent meter, and aim to evoke the emotions associated with the theme. Provide your poem in plain text format, with each line separated by a newline character."""
        else:
            instructions = f"""Your task is to analyze the following poem:\n\n{t['poem']}\n\nProvide a detailed analysis of the poem in terms of its structure, theme, and emotional impact. Your analysis should be at least 100 words long and provide insights into how the poem achieves its emotional effect. Ensure your analysis is coherent and well-structured."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "theme" in t:
            criteria = [
                "The poem should be at least 8 lines long.",
                "The poem should maintain a consistent meter.",
                "The poem should evoke emotions associated with the theme."
            ]
        else:
            criteria = [
                "The analysis should be at least 100 words long.",
                "The analysis should address the structure, theme, and emotional impact of the poem.",
                "The analysis should provide insights into how the poem achieves its emotional effect.",
                "The analysis should be coherent and well-structured."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
