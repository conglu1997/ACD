class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "art_piece": "A painting with swirling, vibrant colors, heavy brushstrokes, and a sense of movement. The scene depicts a starry night sky over a small village.",
                "style": "Post-Impressionism"
            },
            "2": {
                "art_piece": "A painting with geometric shapes, bold colors, and a sense of abstraction. The scene depicts musicians playing instruments in a colorful, fragmented space.",
                "style": "Cubism"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Identify the style and characteristics of the given piece of art, and then create a description of a new piece of art in the same style.

Art Piece: {t['art_piece']}

Your response should include:
1. Identification of the art style.
2. Description of the key characteristics of the art style, including techniques, typical subjects, and color palettes.
3. A description of a new piece of art that you create in the same style, including the subject matter, composition, and artistic elements used. Be detailed and ensure your description captures the essence of the style.

Example response format:
- Art Style: [Identified art style]
- Characteristics: [Key characteristics of the art style]
- New Art Description: [Description of the new piece of art in the same style]

Ensure your descriptions are vivid, accurate, and coherent, capturing the essence of the art style."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The identified art style should be accurate.",
            "The characteristics of the art style should be well-described and accurate.",
            "The new art description should be coherent and adhere to the identified art style.",
            "The new art description should include detailed subject matter, composition, and artistic elements that reflect the identified style."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
