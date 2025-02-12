class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"artwork": "A painting of a serene landscape with mountains in the background, a river flowing through the middle, and a small cottage near the riverbank."},
            "2": {"artwork": "A surrealist painting featuring melting clocks draped over tree branches and a distorted face in the background."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and describe the following piece of artwork: '{t["artwork"]}'. Your analysis should include the following components:

1. Visual Elements: Describe the key visual elements present in the artwork (e.g., colors, shapes, objects).
2. Themes: Identify and discuss the central themes or messages conveyed by the artwork.
3. Interpretations: Provide possible interpretations of the artwork's meaning or significance.
4. Emotional Impact: Discuss the emotional impact the artwork might have on viewers.

Submit your analysis as a plain text string in paragraph format. Ensure that each component is clearly addressed and your analysis is coherent and insightful."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should describe the key visual elements.",
            "The analysis should identify and discuss the central themes.",
            "The analysis should provide possible interpretations of the artwork's meaning.",
            "The analysis should discuss the emotional impact on viewers.",
            "Each component should be clearly addressed.",
            "The analysis should be coherent and insightful."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
