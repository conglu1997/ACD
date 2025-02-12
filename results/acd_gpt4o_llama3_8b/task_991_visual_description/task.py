class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "A bustling city street during a rainy night."},
            "2": {"prompt": "A serene mountain landscape at sunrise."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t["prompt"]
        return f"""Generate a vivid and detailed description of an image based on the following prompt: '{prompt}'. Your description should be engaging and paint a clear picture in the reader's mind. Use rich and evocative language, and ensure that the description is coherent and logically structured. Avoid repetition and provide a unique perspective throughout the description. Submit your description as a plain text string in the following format:\nDescription: [Your description here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should be based on the given prompt.",
            "The description should be vivid and detailed.",
            "The description should be engaging and logically structured.",
            "The description should paint a clear picture in the reader's mind.",
            "The description should avoid repetition and provide a unique perspective."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
