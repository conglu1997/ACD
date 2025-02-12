class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Recreate the signing of the Declaration of Independence. Include key figures, the context leading to the event, and its significance.",
                "instructions": "Recreate a detailed narrative of the signing of the Declaration of Independence. Include key figures such as Thomas Jefferson, John Adams, and Benjamin Franklin, the context leading to the event, and its significance in American history. Ensure that your narrative is historically accurate, engaging, and coherent. The total word count should be between 500 to 700 words. Submit your response as a plain text string."
            },
            "2": {
                "prompt": "Recreate the fall of the Berlin Wall. Include key figures, the context leading to the event, and its significance.",
                "instructions": "Recreate a detailed narrative of the fall of the Berlin Wall. Include key figures such as Mikhail Gorbachev and Ronald Reagan, the context leading to the event, and its significance in world history. Ensure that your narrative is historically accurate, engaging, and coherent. The total word count should be between 500 to 700 words. Submit your response as a plain text string."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Recreate a detailed narrative of the historical event based on the following prompt: '{t['prompt']}'. Include key figures, the context leading to the event, and its significance. Ensure that your narrative is historically accurate, engaging, and coherent. The total word count should be between 500 to 700 words. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The narrative should be historically accurate.",
            "The narrative should include key figures and the context leading to the event.",
            "The narrative should explain the significance of the event.",
            "The total word count should be between 500 to 700 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
