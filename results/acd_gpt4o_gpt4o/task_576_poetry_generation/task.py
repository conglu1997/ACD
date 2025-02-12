class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "hope",
                "emotion": "uplifting"
            },
            "2": {
                "theme": "loss",
                "emotion": "melancholy"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        emotion = t["emotion"]
        instructions = f"""Your task is to generate a poem based on the given theme and emotion.

Theme: {theme}
Emotion: {emotion}

Your poem should:
1. Be creative and coherent.
2. Evoke the specified emotion in the reader.
3. Adhere to the theme provided.

Provide your poem in plain text format, ensuring that it is evocative and well-structured.
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The poem should be creative and coherent.",
            "The poem should effectively evoke the specified emotion.",
            "The poem should adhere to the given theme.",
            "The poem should be well-structured and evocative."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
