class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"traits": ["introverted", "analytical", "perfectionist"]},
            "2": {"traits": ["extroverted", "spontaneous", "empathetic"]},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        traits = ', '.join(t['traits'])
        return f"""Your task is to create a detailed psychological profile for a fictional character based on the following traits:

Traits: {traits}

Ensure that the profile includes the character's background, personality, strengths, weaknesses, motivations, and typical behavior. The profile should be coherent, detailed, and reflect a deep understanding of the given traits. Provide the profile in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The profile should be coherent.", "The profile should be detailed.", "The profile should accurately reflect the given traits.", "The profile should include the character's background, personality, strengths, weaknesses, motivations, and typical behavior."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
