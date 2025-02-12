class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "Imagine a bustling marketplace in a small medieval village. Describe the scene in detail, including the sights, sounds, and activities taking place."},
            "2": {"description": "A serene lakeside at dawn with mist rising from the water, a lone fisherman in a small boat casting a line, and birds starting to chirp as the first light of day breaks over the horizon."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "scenario" in t:
            return f"Your task is to generate a detailed textual description of the following visual scene based on the given scenario:\n\nScenario: {t['scenario']}\n\nEnsure your description is vivid, includes sensory details (sights, sounds, smells), and paints a clear picture of the scene. Provide your response in plain text format."
        elif "description" in t:
            return f"Your task is to interpret the following textual description and recreate the imagined visual scene in your own words:\n\nDescription: {t['description']}\n\nEnsure your interpretation captures all key elements of the scene, includes sensory details, and is written in a clear and vivid manner. Provide your response in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should be vivid and detailed.",
            "The description should include sensory details (sights, sounds, smells).",
            "The description should clearly paint a picture of the scene."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
