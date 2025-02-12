class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"context": "a bustling city street at night"},
            "2": {"context": "a quiet beach at sunrise"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to generate a vivid and rich description of the following sensory experience based on the given context:

Context: {t['context']}

Ensure your description includes visual, auditory, olfactory, tactile, and gustatory details. Aim to create a multi-sensory experience that immerses the reader in the scene. Your response should be at least 100 words long."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should include visual details (e.g., colors, shapes, lighting).",
            "The description should include auditory details (e.g., sounds, noises, music).",
            "The description should include olfactory details (e.g., smells, scents).",
            "The description should include tactile details (e.g., textures, temperatures).",
            "The description should include gustatory details (e.g., tastes if applicable).",
            "The description should be at least 100 words long."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
