class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"criteria": "Create a surrealistic painting that features a floating clock, a melting staircase, and a background of a stormy sea."},
            "2": {"criteria": "Create a futuristic cityscape drawing with flying cars, towering skyscrapers, and a vibrant sunset."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate and describe a piece of visual art based on the following criteria:

{t["criteria"]}

Your description should include:

1. A detailed description of the main elements of the artwork.
2. The style and medium of the artwork (e.g., painting, drawing, digital art).
3. The mood or atmosphere conveyed by the artwork.
4. Any symbolic or thematic elements included in the artwork.

Submit your description as a plain text string in the following format:

Main Elements: [Describe the main elements]
Style and Medium: [Describe the style and medium]
Mood: [Describe the mood or atmosphere]
Symbolism: [Describe any symbolic or thematic elements included]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should include a detailed depiction of the main elements of the artwork.",
            "The description should specify the style and medium of the artwork.",
            "The description should convey the mood or atmosphere of the artwork.",
            "The description should mention any symbolic or thematic elements included in the artwork."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
