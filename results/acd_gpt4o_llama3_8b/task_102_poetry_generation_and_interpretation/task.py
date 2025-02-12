class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "solitude"
            },
            "2": {
                "poem": "The woods are lovely, dark and deep,\nBut I have promises to keep,\nAnd miles to go before I sleep,\nAnd miles to go before I sleep.\n- Robert Frost"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "theme" in t:
            return f"""Generate a poem based on the following theme: {t['theme']}. The poem should be at least 8 lines long and utilize poetic devices such as rhyme, meter, and imagery. Submit your poem as a plain text string. Format: \nLine 1\nLine 2\n...\nLine 8."""
        elif "poem" in t:
            return f"""Interpret the following poem and explain its meaning and style. Ensure your interpretation covers the themes, emotions, and poetic devices used in the poem. Submit your interpretation as a plain text string. Format: \nThemes: ...\nEmotions: ...\nPoetic Devices: ...\n\n{t['poem']}"""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "theme" in t:
            validation_criteria = [
                "The poem should be at least 8 lines long.",
                "The poem should utilize poetic devices such as rhyme, meter, and imagery.",
                "The poem should reflect the given theme."
            ]
        else:
            validation_criteria = [
                "The interpretation should cover the themes, emotions, and poetic devices used in the poem.",
                "The interpretation should be coherent and logically structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
