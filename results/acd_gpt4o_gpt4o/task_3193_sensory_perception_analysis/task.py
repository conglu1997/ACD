class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "Imagine you are standing on a beach at sunset. Describe the sensory experience in detail, including what you see, hear, smell, and feel."},
            "2": {"scenario": "You are in a bustling city market. Describe the sensory experience in detail, including what you see, hear, smell, and feel."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to describe the following sensory experience based on the given scenario:\n\n{t['scenario']}\n\nYour description should be vivid and detailed, capturing the essence of what you see, hear, smell, and feel. Use descriptive language to convey the sensory details effectively. Submit your description in plain text format.\n\nFormat your response as follows:\n\nSensory Description: [Your detailed description]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should be vivid and detailed, capturing the essence of the sensory experience.",
            "The submission should include details of what is seen, heard, smelled, and felt.",
            "The language used should be descriptive and effective in conveying the sensory details."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
