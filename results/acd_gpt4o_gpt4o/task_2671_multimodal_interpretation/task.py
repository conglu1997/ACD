class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "artwork_description": "A surrealist painting featuring melting clocks and a barren landscape.",
                "music_description": "A classical piece with a slow tempo and melancholic melody.",
                "expected_theme": "The passage of time and existential reflection"
            },
            "2": {
                "artwork_description": "An abstract painting with bold, chaotic brushstrokes and vibrant colors.",
                "music_description": "A jazz composition with an energetic, improvisational style.",
                "expected_theme": "Chaos and spontaneity"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret and relate the following pieces of visual art and music. Analyze their elements and explain how they convey the given theme or emotion.

Artwork Description: {t['artwork_description']}

Music Description: {t['music_description']}

Provide a detailed analysis in plain text format. Your analysis should include:
1. The elements of the artwork that contribute to the theme or emotion, with specific examples.
2. The elements of the music that contribute to the theme or emotion, with specific examples.
3. How the artwork and music together convey the given theme or emotion, with detailed explanations."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis includes elements of the artwork that contribute to the theme or emotion, with specific examples.",
            "The analysis includes elements of the music that contribute to the theme or emotion, with specific examples.",
            "The analysis explains how the artwork and music together convey the given theme or emotion, with detailed explanations."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
