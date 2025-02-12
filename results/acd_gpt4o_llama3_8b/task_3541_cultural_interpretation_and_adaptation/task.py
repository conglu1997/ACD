class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"original_culture": "Japanese", "story": "The Tale of the Bamboo Cutter", "target_culture": "Ancient Greek"},
            "2": {"original_culture": "Norse", "story": "The Legend of Thor", "target_culture": "Indian"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are tasked with interpreting a cultural story or tradition from one culture and adapting it to a different cultural context while maintaining the core elements of the original story.

Original Culture: {t['original_culture']}
Story: {t['story']}
Target Culture: {t['target_culture']}

Your task is to rewrite the given story as if it originated in the target culture. Ensure that the adaptation reflects the values, norms, and elements typical of the target culture while preserving the core plot and characters of the original story. Submit your adaptation as a plain text string.

Example format:

Adapted Story:
[Your adapted story here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The adaptation should reflect the values, norms, and elements typical of the target culture.", "The core plot and characters of the original story should be preserved."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
