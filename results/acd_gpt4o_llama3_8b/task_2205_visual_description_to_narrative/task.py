class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "A bustling marketplace on a sunny day with vendors selling fruits, vegetables, and handmade crafts. Children running around, a street musician playing a violin, and an artist painting a mural."},
            "2": {"description": "A serene beach at sunset with waves gently crashing, a couple walking hand in hand, a group of friends having a bonfire, and a lone surfer catching the last wave of the day."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Convert the following detailed visual description into a coherent and engaging narrative. Your narrative should capture the essence of the scene, include vivid details, and be at least 200 words long. Submit your narrative as a plain text string.

Visual Description: {t["description"]}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The narrative should capture the essence of the scene.", "The narrative should include vivid details.", "The narrative should be at least 200 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
