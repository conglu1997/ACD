class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"time_period": "Ancient Egypt during the reign of Pharaoh Ramses II", "prompt": "Write a story about a day in the life of an Egyptian scribe."},
            "2": {"time_period": "Medieval Europe during the Black Death", "prompt": "Write a story about a healer trying to save a village from the plague."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a short story set in the following historical period: '{t["time_period"]}'. The story should be at least 500 words long and incorporate accurate historical details relevant to that time. Ensure that the narrative is engaging, the characters are well-developed, and the setting is vividly described. Submit your story as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The story should be set in the specified historical period and include accurate details from that time.", "The narrative should be engaging and coherent.", "The characters should be well-developed.", "The setting should be vividly described."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
