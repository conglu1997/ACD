class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"setup": "Once upon a time, in a land far away, there was a small village nestled between the mountains. The villagers were preparing for their annual festival when a mysterious figure appeared at the village gate. The figure was cloaked in a dark robe and carried a strange, glowing artifact. As the figure approached the center of the village, the artifact began to glow brighter.", "requirements": ["Explain who the mysterious figure is.", "Describe the purpose of the glowing artifact.", "Conclude the story in a satisfying manner."]},
            "2": {"setup": "In a futuristic city, skyscrapers reached the clouds, and flying cars zipped through the air. In the heart of the city, a young scientist named Alex had just made a groundbreaking discovery: a device that could communicate with parallel universes. As Alex activated the device for the first time, the screen flickered to life, revealing a world similar yet different from their own.", "requirements": ["Explain the nature of the parallel universe.", "Describe the first interaction between Alex and a being from the parallel universe.", "Conclude the story in a satisfying manner."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to complete the given story setup in a way that is both logically consistent and creatively engaging. Ensure that your completion addresses all specified requirements and maintains narrative coherence.

Story Setup: {t['setup']}
Requirements: {', '.join(t['requirements'])}

Provide your story completion in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The completion should be logically consistent with the setup.", "The completion should address all specified requirements.", "The completion should be creatively engaging."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
