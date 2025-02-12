class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "The concept of time as a sentient being.", "example_story": "Once upon a time, in a realm where minutes had minds, Time decided it had enough of being chased. It longed to explore, to wander without the pressure of ticking clocks and deadlines..."},
            "2": {"theme": "A world where emotions are physical objects.", "example_story": "In a land where joy could be bottled and sorrow could be swept away, young Lyra discovered the secret to capturing the essence of hope. It shimmered like a delicate glass sculpture, fragile but powerful..."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a fictional narrative based on the following abstract theme:

{t['theme']}

Ensure that your narrative is coherent, engaging, and explores the given theme in a creative manner. Submit your narrative as a plain text string with the prefix 'Narrative:'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The narrative should be coherent and engaging.", "The story should explore the given theme creatively."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0