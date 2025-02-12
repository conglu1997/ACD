class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"character": "Alice", "emotion": "heartbreak"},
            "2": {"character": "Bob", "emotion": "triumph"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        character = t["character"]
        emotion = t["emotion"]
        instructions = f"""Your task is to write a letter from the perspective of a fictional character experiencing a specific emotion.

Character: {character}
Emotion: {emotion}

In your letter, you should:
1. Clearly convey the character's emotional state.
2. Provide context or events that led to this emotional state.
3. Use expressive language to reflect the character's feelings.
4. Maintain coherence and narrative flow.

Your response should be detailed, well-structured, and demonstrate a clear understanding of the character's perspective and emotions. Format your response as follows:

Dear [Recipient],

[Body of the letter]

Sincerely,
[Character's Name]
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The letter should clearly convey the character's emotional state.",
            "The context or events leading to the emotional state should be provided.",
            "The language should be expressive and reflect the character's feelings.",
            "The letter should maintain coherence and narrative flow."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
