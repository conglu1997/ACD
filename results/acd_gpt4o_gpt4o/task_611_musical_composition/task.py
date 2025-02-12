class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"genre": "classical", "mood": "melancholic", "instruments": "piano, violin"},
            "2": {"genre": "jazz", "mood": "upbeat", "instruments": "saxophone, drums, bass"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        genre = t["genre"]
        mood = t["mood"]
        instruments = t["instruments"]
        instructions = f"""Your task is to compose a piece of music based on the following criteria:

Genre: {genre}
Mood: {mood}
Instruments: {instruments}

Provide a detailed description of the musical piece, including the melody, harmony, rhythm, and structure. Ensure that the composition aligns with the specified genre, mood, and instruments. Your response should be structured as follows:

1. Melody: [Describe the melody]
2. Harmony: [Describe the harmony]
3. Rhythm: [Describe the rhythm]
4. Structure: [Describe the overall structure of the composition]

Ensure that each section is clearly labeled and explained."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The composition should align with the specified genre.",
            "The composition should reflect the given mood.",
            "The composition should incorporate the mentioned instruments.",
            "The musical elements such as melody, harmony, rhythm, and structure should be well-defined and appropriate for the genre.",
            "The description should be detailed and coherent.",
            "Each section (melody, harmony, rhythm, structure) should be clearly labeled and explained."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
