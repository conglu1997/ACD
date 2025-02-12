class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "time"},
            "2": {"topic": "love"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate two creative metaphors and two creative similes based on the following topic: '{t["topic"]}'. A metaphor is a figure of speech that directly refers to one thing by mentioning another, and a simile is a figure of speech that compares two things using 'like' or 'as'. Ensure that your metaphors and similes are original, vivid, and contextually appropriate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submission should include two metaphors and two similes.",
            "The metaphors and similes should be original and creative.",
            "The metaphors and similes should be contextually appropriate to the given topic."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
