class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "topic": "Explain the process of photosynthesis in plants in the form of a short story suitable for children. Ensure the story is engaging, scientifically accurate, and easy to understand. Submit your response as a plain text string in story format."
            },
            "2": {
                "topic": "Describe how black holes form and their impact on the surrounding space in the form of a narrative suitable for a general audience. Ensure the explanation is engaging, scientifically accurate, and captivating. Submit your response as a plain text string in narrative format."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a scientifically accurate yet creative explanation of the following topic:

{t['topic']}

Ensure your explanation is engaging, easy to understand, and scientifically accurate. Submit your response as a plain text string in the specified format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should be scientifically accurate.",
            "The explanation should be engaging and easy to understand.",
            "The explanation should be coherent and well-structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
