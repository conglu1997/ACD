class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"context": "Ancient Egypt during the reign of Pharaoh Ramses II.", "character": "A young scribe learning the ways of the court."},
            "2": {"context": "Medieval Europe during the Black Plague.", "character": "A healer trying to save her village."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a historical story based on the given context and character.

Context: {t['context']}
Character: {t['character']}

Instructions:
1. Create a detailed and engaging story set in the given historical context.
2. Incorporate accurate historical facts and details relevant to the time period.
3. Develop the character and their interactions within the historical setting.
4. Ensure that the story is coherent, creative, and immersive.

Your response should be in the following format:
Historical Story: [Your story]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The story should be set in the given historical context.", "The story should incorporate accurate historical facts relevant to the time period.", "The character should be well-developed and interact naturally within the historical setting.", "The story should be coherent, creative, and immersive."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
