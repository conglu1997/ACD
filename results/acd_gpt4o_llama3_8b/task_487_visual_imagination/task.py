class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"visual_description": "A serene lakeside at twilight, with a small wooden dock extending into the water, surrounded by tall pine trees. The sky is painted in hues of orange and purple, reflecting off the calm lake surface. Nearby, a family of ducks swims by, creating gentle ripples in the water. In the distance, a log cabin with smoke rising from its chimney can be seen."},
            "2": {"visual_description": "A bustling medieval marketplace, filled with merchants selling their wares, colorful tents, and people in period clothing. The air is filled with the sounds of bartering and the aroma of various foods. In the center, a juggler performs tricks while a crowd gathers to watch. To the side, a blacksmith hammers away at his forge, with sparks flying."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following visual description and generate a corresponding text that describes an imaginary scene in detail:

Visual Description: {t['visual_description']}

Ensure that your description is vivid, coherent, and captures the essence of the visual description provided. Your description should also include at least three distinct elements mentioned in the visual description. Use descriptive language to bring the scene to life. Submit your description as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should be vivid and coherent.", "The description should accurately capture the essence of the visual description provided.", "The description should include at least three distinct elements mentioned in the visual description."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
