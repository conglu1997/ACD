class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "friendship", "style": "fable", "constraints": "The story must include a moral lesson and feature animal characters."},
            "2": {"theme": "betrayal", "style": "noir", "constraints": "The story must be set in a city and involve a detective character."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        style = t["style"]
        constraints = t["constraints"]
        instructions = f"""Your task is to create a short story based on the following constraints:\n\n- Theme: {theme}\n- Style: {style}\n- Additional Constraints: {constraints}\n\nEnsure that your story adheres to the given theme and style, and meets all the constraints provided. The story should be at least 300 words long and should be coherent and engaging. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should adhere to the given theme and style.",
            "The story should meet all the specified constraints.",
            "The story should be coherent and engaging."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
