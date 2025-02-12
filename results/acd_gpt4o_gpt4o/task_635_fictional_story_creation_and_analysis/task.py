class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a short story about a time-traveling detective."},
            "2": {"story": "Once upon a time in a faraway land, there was a young knight who discovered a magical sword. The sword had the power to grant any wish, but it also had a dark secret..."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "prompt" in t:
            return f"""Your task is to write a fictional short story based on the following prompt:

{t["prompt"]}

Your story should be engaging, well-structured, and demonstrate good use of language. Ensure it has a clear beginning, middle, and end. Aim for a word count between 500 and 1000 words. Format your response in plain text."""
        elif "story" in t:
            return f"""Your task is to analyze the following fictional story:

{t["story"]}

In your analysis, you should:
1. Identify the main theme of the story.
2. Discuss the development of the main character.
3. Explain the structure of the plot and any notable plot points.
4. Provide a brief critique of the story, highlighting its strengths and areas for improvement.

Ensure your analysis is detailed, well-structured, and demonstrates a good understanding of literary concepts. Format your response in plain text. Your analysis should be between 300 and 500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "prompt" in t:
            criteria = [
                "The story should be engaging and well-structured.",
                "The story should have a clear beginning, middle, and end.",
                "The story should demonstrate good use of language.",
                "The story should be between 500 and 1000 words.",
            ]
        elif "story" in t:
            criteria = [
                "The analysis should identify the main theme of the story.",
                "The analysis should discuss the development of the main character.",
                "The analysis should explain the structure of the plot and any notable plot points.",
                "The analysis should provide a brief critique of the story, highlighting its strengths and areas for improvement.",
                "The analysis should be detailed and well-structured.",
                "The analysis should be between 300 and 500 words.",
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
