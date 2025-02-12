class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"input_style": "modern", "output_style": "archaic", "text": "In the midst of the bustling city, a young man named John hurried through the crowded streets, his mind racing with thoughts of his impending job interview."},
            "2": {"input_style": "formal", "output_style": "casual", "text": "We would like to inform you that your application has been reviewed and we are pleased to extend an invitation for you to attend an interview at our headquarters."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        input_style = t["input_style"]
        output_style = t["output_style"]
        text = t["text"]
        instructions = f"""Your task is to transform the following text from {input_style} style to {output_style} style:

Text: {text}

Ensure that the transformed text accurately captures the essence and meaning of the original text while reflecting the specified style. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The transformed text should accurately capture the essence and meaning of the original text.", "The transformed text should reflect the specified style appropriately."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
