class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "photosynthesis", "instruction": "Create a story that explains the process of photosynthesis. The story should be engaging, accurate, and suitable for a middle school audience."},
            "2": {"concept": "Newton's first law of motion", "instruction": "Create a story that explains Newton's first law of motion. The story should be engaging, accurate, and suitable for a middle school audience."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to create a story that explains the following scientific concept:

Concept: {t['concept']}

Instruction: {t['instruction']}

Ensure that the story is engaging, accurate, and suitable for a middle school audience. Provide your story in plain text format.

Example Response Format:
Title: [Your Story Title]
Story: [Your Story Text]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should accurately explain the scientific concept.",
            "The story should be engaging and suitable for a middle school audience.",
            "The story should be creative and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
