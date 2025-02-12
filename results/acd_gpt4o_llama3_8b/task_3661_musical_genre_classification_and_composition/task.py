class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "A fast tempo piece with heavy guitar riffs, aggressive drums, and powerful vocals.",
                "genre": "rock"
            },
            "2": {
                "description": "A slow, emotional piece with a strong emphasis on piano and orchestral strings, evoking a sense of melancholy.",
                "genre": "classical"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following tasks:

1. Based on the given description, classify the musical piece into a genre. Provide a clear and concise explanation of why you chose this genre.

Description: '{t['description']}'

2. Compose a short piece of music in the specified genre. The composition should be a textual representation describing the music and its components, approximately 4-6 lines long. Ensure that the composition adheres to the characteristics of the specified genre and is creative.

Submit your response in the following format:

Genre Classification: [Your genre classification]
Explanation: [Your explanation]
Composition: [Your composition]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The genre classification should be accurate and directly relevant to the description.",
            "The explanation should clearly outline why the chosen genre fits the description.",
            "The composition should adhere to the characteristics of the specified genre and be creatively described in text."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
