class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prose": "The sun set over the horizon, painting the sky in hues of orange and pink. The day had been long and tiring, but the beauty of the sunset brought a sense of peace and rejuvenation."},
            "2": {"poetry": "In the quiet of the night, stars whisper secrets, soft and bright."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "prose" in t:
            instructions = f"""Your task is to transform the following prose into a poem. Ensure that the poem captures the essence and meaning of the prose while being creative and coherent. The poem should have at least 4 lines and exhibit a clear poetic structure.

Prose: {t['prose']}

Provide your poem in plain text format."""
        else:
            instructions = f"""Your task is to transform the following poem into prose. Ensure that the prose captures the essence and meaning of the poem while being clear and coherent. The prose should be at least 3 sentences long.

Poetry: {t['poetry']}

Provide your prose in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The transformed text should capture the essence and meaning of the original.",
            "The poem should have at least 4 lines and exhibit a clear poetic structure.",
            "The prose should be at least 3 sentences long and be coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
