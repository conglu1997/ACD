class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"constraints": "The story must include a detective, a hidden treasure, and a false accusation. The story should also have at least one plot twist."},
            "2": {"constraints": "The story must include a spaceship, an alien species, and a diplomatic mission. The story should also involve an unexpected technological failure."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a coherent and logically consistent short story based on the following constraints: {t["constraints"]}. Ensure that the story follows a clear narrative structure, with a beginning, middle, and end, and that all elements mentioned in the constraints are meaningfully included. Include at least one dialogue exchange between characters. Submit your story in plain text format as follows:

Story: [Your story here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story must include all elements mentioned in the constraints.",
            "The story should have a clear narrative structure with a beginning, middle, and end.",
            "The story should be logically consistent and coherent.",
            "The story should include at least one dialogue exchange between characters."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
