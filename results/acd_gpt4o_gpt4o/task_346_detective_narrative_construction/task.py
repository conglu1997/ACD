class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"clues": ["A broken window", "A red scarf", "Footprints in the garden"], "type": "create"},
            "2": {"narrative": "Detective Jane arrived at the crime scene and noticed the broken window. She found a red scarf nearby and followed the footprints in the garden to the back gate.", "type": "analyze"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "create":
            return f"""Your task is to create a detective story based on the following clues: {', '.join(t["clues"])}. Ensure your story is logically coherent, follows genre-specific conventions, and concludes with a plausible resolution. The story should be between 200-300 words. Provide your story in a narrative format."""
        else:
            return f"""Your task is to analyze the following detective narrative: '{t["narrative"]}'. Identify any logical inconsistencies or plot holes and suggest improvements to make the story more coherent. Provide your analysis in 2-3 sentences."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "create":
            criteria = ["The story should be logically coherent, follow genre-specific conventions, and conclude with a plausible resolution."]
        else:
            criteria = ["The analysis should accurately identify logical inconsistencies or plot holes and suggest reasonable improvements."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
