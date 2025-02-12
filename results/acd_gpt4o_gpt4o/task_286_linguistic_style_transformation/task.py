class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "text": "Dear Sir/Madam, I hope this message finds you well. I am writing to remind you about the upcoming meeting scheduled for next Monday at 10 AM. Kindly ensure your presence and be prepared with the necessary documents.",
                "target_style": "informal"
            },
            "2": {
                "text": "Hey buddy, just a heads up about the meeting next Monday at 10 AM. Make sure you're there and don't forget to bring the stuff we talked about.",
                "target_style": "formal"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        text = t["text"]
        target_style = t["target_style"]
        instructions = f"""Your task is to transform the given text into a {target_style} style while preserving its meaning. Here is the text:

{text}

Submit your transformed text in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The transformed text should match the target style.",
            "The meaning of the original text should be preserved."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
