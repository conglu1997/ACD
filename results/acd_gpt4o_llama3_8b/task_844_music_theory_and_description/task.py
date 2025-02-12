class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "musical_prompt": "Describe the emotional impact and common uses of a minor chord in music composition."
            },
            "2": {
                "musical_prompt": "Explain the concept of syncopation and provide an example of how it can be used in a musical piece."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following musical concept and generate a description based on the given prompt:

Musical Prompt: '{t['musical_prompt']}'

Ensure that your description is clear, detailed, and demonstrates a solid understanding of the musical concept. Submit your response as a plain text string in the following format:

Description: [Your description]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The description must accurately interpret the musical concept.",
            "The description must be clear and detailed.",
            "The description must demonstrate understanding of the musical concept."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
