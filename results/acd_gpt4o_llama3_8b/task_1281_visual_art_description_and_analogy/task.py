class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "art_description": "A serene landscape with rolling hills, a calm lake reflecting the blue sky, and a lone tree standing by the water's edge. The colors are soft pastels, and the scene evokes a sense of tranquility and peace.",
                "task": "Generate an analogy for this visual art description that compares it to an emotional state or a moment in time."
            },
            "2": {
                "art_description": "A bustling cityscape at dusk, with skyscrapers illuminated by the golden hues of the setting sun. The streets are filled with people and cars, and the energy of the city is palpable. The colors are vibrant and dynamic.",
                "task": "Write a new description of a different scene that evokes a similar sense of energy and vibrancy as the cityscape."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following description of visual art: '{t['art_description']}'.

Task: {t['task']}

Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The analogy or new description should be relevant to the given art description.",
            "The response should be creative and demonstrate a deep understanding of the given art description.",
            "The language used should be vivid and evocative, capturing the essence of the original description."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
