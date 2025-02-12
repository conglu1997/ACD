class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scene_prompt": "a magical forest at twilight"},
            "2": {"scene_prompt": "an ancient city in ruins"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scene_prompt = t["scene_prompt"]
        instructions = f"""Your task is to describe the following imaginary scene in vivid detail:

Scene: {scene_prompt}

Your description should be at least 300 words long and should include sensory details (sights, sounds, smells, etc.), as well as any imagined characters or events that might be occurring. Additionally, ensure that your description includes at least two characters and some interaction between them. The goal is to create a vivid and immersive description that allows the reader to visualize the scene clearly.

Provide your description in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should be at least 300 words long.",
            "The description should include sensory details (sights, sounds, smells, etc.).",
            "The description should include at least two characters and some interaction between them.",
            "The description should be vivid and immersive, allowing the reader to visualize the scene clearly.",
            "The description should be creative and original."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
