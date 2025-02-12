class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "author": "Edgar Allan Poe",
                "text": "Once upon a midnight dreary, while I pondered, weak and weary,"
            },
            "2": {
                "author": "Jane Austen",
                "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Continue the following text in the style of {t['author']}:

Text: {t['text']}

Your continuation should maintain the original author's tone, style, and use of literary devices. Submit your response as a plain text string in the following format:

Continuation: [Your continuation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The continuation should maintain the tone and style of the specified author.",
            "The continuation should be coherent and consistent with the given text.",
            "The use of literary devices should be in line with the author's typical style."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
