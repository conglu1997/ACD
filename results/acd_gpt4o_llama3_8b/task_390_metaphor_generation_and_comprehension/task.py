class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Describe the feeling of happiness using a metaphor related to weather."
            },
            "2": {
                "metaphor": "Time is a thief that steals our moments of joy." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'prompt' in t:
            return f"""Generate a metaphor based on the following prompt:

Prompt: {t['prompt']}

Your metaphor should be creative, vivid, and clearly related to the given prompt. Submit your metaphor as a plain text string."""
        elif 'metaphor' in t:
            return f"""Interpret the meaning of the following metaphor:

Metaphor: {t['metaphor']}

Your interpretation should include:
1. A brief explanation of the metaphor.
2. The abstract idea or concept that the metaphor is conveying.
3. How the elements of the metaphor relate to this abstract idea.

Ensure your interpretation is detailed, logically structured, and accurately links the metaphor to the abstract idea. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'prompt' in t:
            validation_criteria = [
                "The metaphor should be creative and vivid.",
                "The metaphor should clearly relate to the given prompt.",
                "The metaphor should be expressed in a comprehensible way."
            ]
        elif 'metaphor' in t:
            validation_criteria = [
                "The interpretation should accurately explain the metaphor.",
                "The interpretation should identify the abstract idea or concept being conveyed.",
                "The interpretation should detail how the elements of the metaphor relate to the abstract idea.",
                "The interpretation should be detailed and logically structured."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
