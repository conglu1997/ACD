class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "original_tale": "Cinderella",
                "new_perspective": "The Stepmother"
            },
            "2": {
                "original_tale": "Little Red Riding Hood",
                "new_perspective": "The Wolf"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Rewrite the classic fairy tale '{t['original_tale']}' from the perspective of '{t['new_perspective']}'. Ensure that the rewritten story is coherent, engaging, and provides a unique viewpoint from the chosen character. Maintain the original plot but add depth and personality to the new narrator's perspective.

Submit your response in the following format:

Title: [Your Title]
Story: [Your Rewritten Story]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The story should be rewritten from the specified character's perspective.",
            "The rewritten story should be coherent and engaging.",
            "The new perspective should add depth and personality to the character.",
            "The original plot should be maintained.",
            "The response should follow the specified format with a title and story."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
