class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event": "The fall of the Berlin Wall",
                "significance": 200
            },
            "2": {
                "event": "The signing of the Treaty of Versailles",
                "significance": 250
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given a historical event: '{t['event']}'. Your task is to write a detailed analysis of the event, explaining its significance in at least {t['significance']} words. Additionally, craft a narrative story that incorporates the event and demonstrates its impact on individuals or society. Ensure that your narrative is engaging, historically accurate, and creatively written. Submit your response as a plain text string with the following sections:

Analysis: [Your detailed analysis]
Story: [Your narrative story]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [f"The analysis should be at least {t['significance']} words long.", "The narrative story should be engaging, historically accurate, and creatively written."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
