class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "visual_description": "A bustling marketplace with various stalls selling fruits, vegetables, and crafts. People are haggling over prices, a street musician is playing a violin, and children are running around playing. The sky is clear and blue, and the sun is shining brightly."
            },
            "2": {
                "visual_description": "A quiet library with rows of bookshelves filled with books. A few people are seated at tables reading or studying. A librarian is helping someone check out a book, and a cat is sleeping on a windowsill. The room is well-lit with soft, warm lighting."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a detailed narrative or description based on the following visual scene description:

{t['visual_description']}

Ensure your narrative is vivid, engaging, and accurately reflects the visual description provided. Use descriptive language to paint a clear picture of the scene. Submit your narrative as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The narrative should be vivid and engaging.",
            "The narrative should accurately reflect the visual description provided.",
            "The language used should be descriptive and paint a clear picture of the scene."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
